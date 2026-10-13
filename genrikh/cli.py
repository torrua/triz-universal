"""
Genrikh CLI Interface.
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
[bold white]G E N R I K H[/bold white] [dim]— Universal Inventive Problem Solver[/dim]
[dim]In honor of Genrikh Saulovich Altshuller (1926–1998), creator of TRIZ[/dim]
[green][SECURE] Open-Source AI (Gemma 2 / Ollama) • 100% Local • Zero Compromises[/green]
"""

def cmd_solve(args):
    console.print(BANNER)
    problem = args.problem
    if not problem:
        problem = Prompt.ask("[bold yellow]Describe the problem / technical or business contradiction[/bold yellow]")
    
    param_a = args.param_a
    if not param_a:
        param_a = Prompt.ask("[bold green]What parameter should be IMPROVED (Speed, Reliability, Scale, Ergonomics)?[/bold green]")
        
    param_b = args.param_b
    if not param_b:
        param_b = Prompt.ask("[bold red]What parameter must NOT WORSEN (Cost, Memory, Battery, Complexity)?[/bold red]")

    with console.status("[bold cyan]Genrikh is analyzing contradiction via ARIZ-AI pipeline...[/bold cyan]"):
        engine = OpenSourceAIEngine()
        result = engine.solve(problem, param_a, param_b, force_offline=args.offline)

    # Layer 1
    console.print("\n")
    console.print(Panel(
        Markdown(result.layer_1),
        title="[bold green]Layer 1: Plain-Language Solution (Zero Jargon)[/bold green]",
        border_style="green",
        expand=False
    ))

    # Voice Briefing with ElevenLabs
    if args.voice:
        with console.status("[bold magenta]Generating voice briefing via ElevenLabs...[/bold magenta]"):
            voice = ElevenLabsVoice()
            audio_file = voice.generate_audio(result.layer_1, "genrikh_briefing.mp3")
            if audio_file:
                console.print(f"[bold magenta]✓ Voice briefing saved: {audio_file}[/bold magenta]")
            else:
                console.print("[dim yellow](ElevenLabs API key not set in ELEVENLABS_API_KEY)[/dim yellow]")

    # Layer 2 Check
    show_passport = args.passport
    if not show_passport:
        show_passport = Confirm.ask(
            "\n[bold cyan]Display detailed engineering TRIZ passport (PC, IFR, VPR resources, principles)?[/bold cyan]",
            default=False
        )

    if show_passport:
        console.print("\n")
        console.print(Panel(
            Markdown(result.layer_2),
            title="[bold cyan]Layer 2: Professional TRIZ Solution Passport[/bold cyan]",
            border_style="cyan",
            expand=False
        ))

    if args.out:
        out_path = Path(args.out)
        content = f"{result.layer_1}\n\n---\n\n{result.layer_2}"
        out_path.write_text(content, encoding="utf-8")
        console.print(f"\n[bold green]✓ Solution saved to {out_path}[/bold green]")

def cmd_consult(args):
    console.print(BANNER)
    consultant = ConsultantSession()

    if args.template:
        template_key = args.template
        if template_key not in TEMPLATES:
            console.print(f"[red]Template not found. Available: {list(TEMPLATES.keys())}[/red]")
            return
        with console.status(f"[bold cyan]Genrikh is executing audit for template '{template_key}'...[/bold cyan]"):
            report = consultant.run_template(template_key)
    else:
        console.print("[bold yellow]Select a standard archetype (or enter a custom project):[/bold yellow]")
        for i, (k, v) in enumerate(TEMPLATES.items(), 1):
            console.print(f"  [cyan]{i}[/cyan]. [bold]{v.project_title}[/bold] ({v.client_name}) - {v.domain}")
        console.print("  [cyan]4[/cyan]. [bold]Custom Project / Individual Audit[/bold]")
        
        choice = Prompt.ask("Selection", choices=["1", "2", "3", "4"], default="1")
        if choice in ["1", "2", "3"]:
            k = list(TEMPLATES.keys())[int(choice) - 1]
            with console.status(f"[bold cyan]Genrikh is solving archetype '{k}'...[/bold cyan]"):
                report = consultant.run_template(k)
        else:
            c_name = Prompt.ask("Client / Project Name")
            p_title = Prompt.ask("Project Title")
            domain = Prompt.ask("Domain (Software, Hardware, Business, Bio)")
            stmt = Prompt.ask("Contradiction Statement")
            p_a = Prompt.ask("Goal (Parameter to Improve)")
            p_b = Prompt.ask("Constraint (Must Not Worsen)")
            proj = ClientProject(
                client_name=c_name, project_title=p_title, domain=domain,
                problem_statement=stmt, target_metric=p_a, constraint_metric=p_b
            )
            with console.status("[bold cyan]Genrikh is generating inventive roadmap...[/bold cyan]"):
                report = consultant.audit(proj)

    md_content = report.to_markdown()
    console.print("\n")
    console.print(Panel(Markdown(md_content), title="[bold green]Audit Report & Inventive Resolution[/bold green]", border_style="green"))

    out_file = args.out or "genrikh_report.md"
    Path(out_file).write_text(md_content, encoding="utf-8")
    console.print(f"\n[bold green]✓ Report successfully saved to: [underline]{out_file}[/underline][/bold green]")

def cmd_matrix(args):
    console.print(BANNER)
    if args.search:
        results = search_parameters(args.search)
        table = Table(title=f"Parameters matching '{args.search}'")
        table.add_column("#", style="cyan", width=4)
        table.add_column("Classical Name", style="magenta")
        table.add_column("Software / IT Analogue", style="green")
        table.add_column("Business Analogue", style="yellow")
        for p in results:
            table.add_row(str(p.id), p.name_en, p.software, p.business)
        console.print(table)
        return

    if args.improve and args.worsen:
        principles = lookup_principles(args.improve, args.worsen)
        table = Table(title=f"Altshuller Matrix Recommendations: Parameter #{args.improve} vs #{args.worsen}")
        table.add_column("#", style="cyan", width=4)
        table.add_column("TRIZ Principle", style="bold green")
        table.add_column("Software / IT Analogue", style="magenta")
        table.add_column("Business Analogue", style="yellow")
        for pr in principles:
            table.add_row(str(pr.id), pr.name_en, pr.software, pr.business)
        console.print(table)
        return

    # Default
    table = Table(title="Core TRIZ Parameters (39 Altshuller Parameters)")
    table.add_column("#", style="cyan", width=4)
    table.add_column("Classical Name", style="magenta")
    table.add_column("Software / System Analogue", style="green")
    for i in [9, 1, 27, 36, 14, 19, 32, 33, 30, 39]:
        p = PARAMETERS[i]
        table.add_row(str(p.id), p.name_en, p.software)
    console.print(table)
    console.print("\n[dim]Usage: genrikh matrix --improve 9 --worsen 1   (Speed vs Memory)[/dim]")
    console.print("[dim]       genrikh matrix --search latency[/dim]")

def cmd_serve(args):
    console.print(BANNER)
    import uvicorn
    from genrikh.web.app import app
    port = args.port or 8000
    console.print(f"[bold green]Starting Genrikh Web UI: http://localhost:{port}[/bold green]")
    uvicorn.run(app, host="0.0.0.0", port=port)

def main():
    parser = argparse.ArgumentParser(description="Genrikh - Universal Inventive Problem Solver on Open-Source AI")
    subparsers = parser.add_subparsers(dest="command")

    # Solve
    p_solve = subparsers.add_parser("solve", help="Resolve technical or business contradiction without compromise")
    p_solve.add_argument("--problem", "-p", help="Problem description")
    p_solve.add_argument("--param-a", "-a", help="Parameter to improve")
    p_solve.add_argument("--param-b", "-b", help="Parameter that must not worsen")
    p_solve.add_argument("--passport", action="store_true", help="Display detailed TRIZ passport immediately")
    p_solve.add_argument("--voice", action="store_true", help="Narrate solution via ElevenLabs")
    p_solve.add_argument("--offline", action="store_true", help="Force offline deterministic engine")
    p_solve.add_argument("--out", "-o", help="Save solution to markdown file")

    # Consult
    p_consult = subparsers.add_parser("consult", help="Generate consulting audit report / roadmap")
    p_consult.add_argument("--template", "-t", choices=list(TEMPLATES.keys()), help="Select pre-built template")
    p_consult.add_argument("--out", "-o", help="Path to save report")

    # Matrix
    p_matrix = subparsers.add_parser("matrix", help="Explore Altshuller Contradiction Matrix")
    p_matrix.add_argument("--improve", type=int, help="ID of improving parameter")
    p_matrix.add_argument("--worsen", type=int, help="ID of worsening parameter")
    p_matrix.add_argument("--search", "-s", help="Search parameters by keyword")

    # Serve
    p_serve = subparsers.add_parser("serve", help="Launch interactive Web Dashboard")
    p_serve.add_argument("--port", type=int, default=8000, help="Web server port")

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
