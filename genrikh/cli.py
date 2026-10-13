"""
Genrikh (Генрих) CLI Interface.
Named in honor of Genrikh Saulovich Altshuller (1926-1998), the creator of TRIZ.
Universal Inventive Problem Solving Companion for Software, Hardware, and Business.
"""

import sys
import argparse
from pathlib import Path

# Force UTF-8 encoding on Windows console where supported
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt, Confirm

from genrikh.engine import OpenSourceAIEngine
from genrikh.consultant import ConsultantSession, TEMPLATES, ClientProject
from genrikh.matrix import PRINCIPLES, PARAMETERS, lookup_principles, search_parameters
from genrikh.voice import ElevenLabsVoice

console = Console(highlight=False)

BANNER = r"""[bold cyan]
   ____ _____ _   _ ____  ___ _  _ _   _ 
  / ___| ____| \ | |  _ \|_ _| |/ / | | |
 | |  _|  _| |  \| | |_) || || ' /| |_| |
 | |_| | |___| |\  |  _ < | || . \|  _  |
  \____|_____|_| \_|_| \_\___|_|\_\_| |_|
[/bold cyan]
[bold white]Г Е Н Р И Х[/bold white] [dim]— Универсальный Изобретательский Партнер[/dim]
[dim]В честь Генриха Сауловича Альтшуллера (1926–1998), создателя ТРИЗ[/dim]
[green][SECURE] Open-Source AI (Gemma 2 / Ollama) • 100% Local • Zero Compromises[/green]
"""

def cmd_solve(args):
    console.print(BANNER)
    problem = args.problem
    if not problem:
        problem = Prompt.ask("[bold yellow]Опишите задачу / техническое или бизнес-противоречие[/bold yellow]")
    
    param_a = args.param_a
    if not param_a:
        param_a = Prompt.ask("[bold green]Что нужно УЛУЧШИТЬ (Скорость, Надежность, Масштаб, Удобство)?[/bold green]")
        
    param_b = args.param_b
    if not param_b:
        param_b = Prompt.ask("[bold red]Что НЕ ДОЛЖНО ухудшиться (Затраты, Память, Батарея, Сложность)?[/bold red]")

    with console.status("[bold cyan]Генрих анализирует противоречие по алгоритму АРИЗ-AI...[/bold cyan]"):
        engine = OpenSourceAIEngine()
        result = engine.solve(problem, param_a, param_b, force_offline=args.offline)

    # Layer 1
    console.print("\n")
    console.print(Panel(
        Markdown(result.layer_1),
        title="[bold green]Layer 1: Решение простым языком (Без жаргона)[/bold green]",
        border_style="green",
        expand=False
    ))

    # Voice Briefing with ElevenLabs
    if args.voice:
        with console.status("[bold magenta]Генерация голосового брифинга через ElevenLabs...[/bold magenta]"):
            voice = ElevenLabsVoice()
            audio_file = voice.generate_audio(result.layer_1, "genrikh_briefing.mp3")
            if audio_file:
                console.print(f"[bold magenta]✓ Голосовой брифинг сохранен: {audio_file}[/bold magenta]")
            else:
                console.print("[dim yellow](ElevenLabs API ключ не задан в ELEVENLABS_API_KEY)[/dim yellow]")

    # Layer 2 Check
    show_passport = args.passport
    if not show_passport:
        show_passport = Confirm.ask(
            "\n[bold cyan]Показать подробный инженерный ТРИЗ-паспорт (ФП, ИКР, ресурсы ВПР, приемы)?[/bold cyan]",
            default=False
        )

    if show_passport:
        console.print("\n")
        console.print(Panel(
            Markdown(result.layer_2),
            title="[bold cyan]Layer 2: Профессиональный ТРИЗ-Паспорт Решения[/bold cyan]",
            border_style="cyan",
            expand=False
        ))

    if args.out:
        out_path = Path(args.out)
        content = f"{result.layer_1}\n\n---\n\n{result.layer_2}"
        out_path.write_text(content, encoding="utf-8")
        console.print(f"\n[bold green]✓ Решение сохранено в {out_path}[/bold green]")

def cmd_consult(args):
    console.print(BANNER)
    consultant = ConsultantSession()

    if args.template:
        template_key = args.template
        if template_key not in TEMPLATES:
            console.print(f"[red]Шаблон не найден. Доступно: {list(TEMPLATES.keys())}[/red]")
            return
        with console.status(f"[bold cyan]Генрих выполняет аудит по шаблону '{template_key}'...[/bold cyan]"):
            report = consultant.run_template(template_key)
    else:
        console.print("[bold yellow]Выберите типовую задачу (или свой кейс):[/bold yellow]")
        for i, (k, v) in enumerate(TEMPLATES.items(), 1):
            console.print(f"  [cyan]{i}[/cyan]. [bold]{v.project_title}[/bold] ({v.client_name}) - {v.domain}")
        console.print("  [cyan]4[/cyan]. [bold]Свой проект / Индивидуальный аудит[/bold]")
        
        choice = Prompt.ask("Выбор", choices=["1", "2", "3", "4"], default="1")
        if choice in ["1", "2", "3"]:
            k = list(TEMPLATES.keys())[int(choice) - 1]
            with console.status(f"[bold cyan]Генрих решает задачу '{k}'...[/bold cyan]"):
                report = consultant.run_template(k)
        else:
            c_name = Prompt.ask("Имя клиента / Проекта")
            p_title = Prompt.ask("Название задачи")
            domain = Prompt.ask("Область (Software, Hardware, Business, Bio)")
            stmt = Prompt.ask("Описание противоречия")
            p_a = Prompt.ask("Что улучшить (Цель)")
            p_b = Prompt.ask("Жесткое ограничение")
            proj = ClientProject(
                client_name=c_name, project_title=p_title, domain=domain,
                problem_statement=stmt, target_metric=p_a, constraint_metric=p_b
            )
            with console.status("[bold cyan]Генрих формирует дорожную карту решения...[/bold cyan]"):
                report = consultant.audit(proj)

    md_content = report.to_markdown()
    console.print("\n")
    console.print(Panel(Markdown(md_content), title="[bold green]Отчет Аудита и Изобретательское Решение[/bold green]", border_style="green"))

    out_file = args.out or "genrikh_report.md"
    Path(out_file).write_text(md_content, encoding="utf-8")
    console.print(f"\n[bold green]✓ Отчет успешно сохранен в: [underline]{out_file}[/underline][/bold green]")

def cmd_matrix(args):
    console.print(BANNER)
    if args.search:
        results = search_parameters(args.search)
        table = Table(title=f"Параметры по запросу '{args.search}'")
        table.add_column("#", style="cyan", width=4)
        table.add_column("Классическое название", style="magenta")
        table.add_column("IT / Программный аналог", style="green")
        table.add_column("Бизнес аналог", style="yellow")
        for p in results:
            table.add_row(str(p.id), f"{p.name_en} ({p.name_ru})", p.software, p.business)
        console.print(table)
        return

    if args.improve and args.worsen:
        principles = lookup_principles(args.improve, args.worsen)
        table = Table(title=f"Рекомендации матрицы Альтшуллера: Параметр #{args.improve} vs #{args.worsen}")
        table.add_column("#", style="cyan", width=4)
        table.add_column("Прием ТРИЗ", style="bold green")
        table.add_column("IT / Софт аналог", style="magenta")
        table.add_column("Бизнес аналог", style="yellow")
        for pr in principles:
            table.add_row(str(pr.id), f"{pr.name_en} / {pr.name_ru}", pr.software, pr.business)
        console.print(table)
        return

    # Default
    table = Table(title="Базовые параметры ТРИЗ (39 параметров Альтшуллера)")
    table.add_column("#", style="cyan", width=4)
    table.add_column("Классическое название", style="magenta")
    table.add_column("IT / Системный аналог", style="green")
    for i in [9, 1, 27, 36, 14, 19, 32, 33, 30, 39]:
        p = PARAMETERS[i]
        table.add_row(str(p.id), f"{p.name_en} ({p.name_ru})", p.software)
    console.print(table)
    console.print("\n[dim]Использование: genrikh matrix --improve 9 --worsen 1   (Скорость vs Память)[/dim]")
    console.print("[dim]              genrikh matrix --search latency[/dim]")

def cmd_serve(args):
    console.print(BANNER)
    import uvicorn
    from genrikh.web.app import app
    port = args.port or 8000
    console.print(f"[bold green]Запуск веб-интерфейса Генриха: http://localhost:{port}[/bold green]")
    uvicorn.run(app, host="0.0.0.0", port=port)

def main():
    parser = argparse.ArgumentParser(description="Генрих (Genrikh) - Универсальный Изобретательский Партнер на Open-Source AI")
    subparsers = parser.add_subparsers(dest="command")

    # Solve
    p_solve = subparsers.add_parser("solve", help="Решить противоречие в любой сфере (софт, железо, бизнес)")
    p_solve.add_argument("--problem", "-p", help="Описание проблемы")
    p_solve.add_argument("--param-a", "-a", help="Параметр, который нужно улучшить")
    p_solve.add_argument("--param-b", "-b", help="Параметр, который нельзя ухудшить")
    p_solve.add_argument("--passport", action="store_true", help="Сразу выводить подробный ТРИЗ-паспорт")
    p_solve.add_argument("--voice", action="store_true", help="Озвучить решение через ElevenLabs")
    p_solve.add_argument("--offline", action="store_true", help="Принудительно использовать автономный движок")
    p_solve.add_argument("--out", "-o", help="Сохранить решение в markdown-файл")

    # Consult
    p_consult = subparsers.add_parser("consult", help="Сформировать отчет аудита / дорожную карту")
    p_consult.add_argument("--template", "-t", choices=list(TEMPLATES.keys()), help="Выбрать готовый шаблон")
    p_consult.add_argument("--out", "-o", help="Путь к файлу для сохранения отчета")

    # Matrix
    p_matrix = subparsers.add_parser("matrix", help="Поиск по матрице противоречий Альтшуллера")
    p_matrix.add_argument("--improve", type=int, help="ID улучшаемого параметра")
    p_matrix.add_argument("--worsen", type=int, help="ID ухудшаемого параметра")
    p_matrix.add_argument("--search", "-s", help="Поиск по ключевому слову")

    # Serve
    p_serve = subparsers.add_parser("serve", help="Запустить веб-интерфейс")
    p_serve.add_argument("--port", type=int, default=8000, help="Порт веб-сервера")

    args = parser.parse_args()
    if args.command == "solve":
        cmd_solve(args)
    elif args.command == "consult":
        cmd_consult(args)
    elif args.command == "matrix":
        cmd_matrix(args)
    elif args.command == "serve":
        cmd_serve(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
