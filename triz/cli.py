"""
TRIZ Universal CLI Interface.
Built with Rich for high-density, beautiful terminal execution.
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

from triz.engine import OpenSourceAIEngine
from triz.consultant import ConsultantSession, TEMPLATES, ClientProject
from triz.matrix import PRINCIPLES, PARAMETERS, lookup_principles, search_parameters

console = Console(highlight=False)

BANNER = r"""[bold cyan]
  _______ _____  _____ ______   _    _       _                            _ 
 |__   __|  __ \|_   _|___  /  | |  | |     (_)                          | |
    | |  | |__) | | |    / /   | |  | |_ __  _ _   _____ _ __ ___  __ _  | |
    | |  |  _  /  | |   / /    | |  | | '_ \| | \ / / _ \ '__/ __|/ _` | | |
    | |  | | \ \ _| |_ / /__   | |__| | | | | |\ V /  __/ |  \__ \ (_| | | |
    |_|  |_|  \_\_____/_____|   \____/|_| |_|_| \_/ \___|_|  |___/\__,_| |_|
[/bold cyan]
[dim]Universal Inventive Problem Solver for Software, Hardware & Solo-Founders[/dim]
[green][SECURE] 100% Local Inference & IP Protection with Open-Source AI[/green]
"""

def cmd_solve(args):
    console.print(BANNER)
    problem = args.problem
    if not problem:
        problem = Prompt.ask("[bold yellow]Describe the technical or business problem / contradiction[/bold yellow]")
    
    param_a = args.param_a
    if not param_a:
        param_a = Prompt.ask("[bold green]What parameter do you want to IMPROVE (Speed, Scale, UX)?[/bold green]")
        
    param_b = args.param_b
    if not param_b:
        param_b = Prompt.ask("[bold red]What parameter CANNOT degrade (Cost, Memory, Battery)?[/bold red]")

    with console.status("[bold cyan]Applying ARIZ-AI Pipeline (Loop 1 State Lock)...[/bold cyan]"):
        engine = OpenSourceAIEngine()
        result = engine.solve(problem, param_a, param_b, force_offline=args.offline)

    # Display Layer 1 (Client / Plain-language Core)
    console.print("\n")
    console.print(Panel(
        Markdown(result.layer_1),
        title="[bold green]Layer 1: Plain-Language Solution (Zero Jargon)[/bold green]",
        border_style="green",
        expand=False
    ))

    # Ask if user wants Layer 2 breakdown (Progressive Disclosure)
    show_passport = args.passport
    if not show_passport:
        show_passport = Confirm.ask(
            "\n[bold cyan]Хотите подробно увидеть ТРИЗ-паспорт решения (АРИЗ-85-В разбор, ФП, ИКР и ресурсы)?[/bold cyan]",
            default=False
        )

    if show_passport:
        console.print("\n")
        console.print(Panel(
            Markdown(result.layer_2),
            title="[bold cyan]Layer 2: Professional TRIZ Passport (Auditable)[/bold cyan]",
            border_style="cyan",
            expand=False
        ))

    if args.out:
        out_path = Path(args.out)
        content = f"{result.layer_1}\n\n---\n\n{result.layer_2}"
        out_path.write_text(content, encoding="utf-8")
        console.print(f"\n[bold green]✓ Saved solution to {out_path}[/bold green]")

def cmd_consult(args):
    console.print(BANNER)
    consultant = ConsultantSession()

    if args.template:
        template_key = args.template
        if template_key not in TEMPLATES:
            console.print(f"[red]Invalid template. Choose from: {list(TEMPLATES.keys())}[/red]")
            return
        with console.status(f"[bold cyan]Running architectural audit for '{template_key}'...[/bold cyan]"):
            report = consultant.run_template(template_key)
    else:
        console.print("[bold yellow]Select a Side Hustle Consulting Archetype:[/bold yellow]")
        for i, (k, v) in enumerate(TEMPLATES.items(), 1):
            console.print(f"  [cyan]{i}[/cyan]. [bold]{v.project_title}[/bold] ({v.client_name}) - {v.domain}")
        console.print("  [cyan]4[/cyan]. [bold]Custom Client Audit Intake[/bold]")
        
        choice = Prompt.ask("Choose option", choices=["1", "2", "3", "4"], default="1")
        if choice in ["1", "2", "3"]:
            k = list(TEMPLATES.keys())[int(choice) - 1]
            with console.status(f"[bold cyan]Auditing {k}...[/bold cyan]"):
                report = consultant.run_template(k)
        else:
            c_name = Prompt.ask("Client / Business Name")
            p_title = Prompt.ask("Project Title")
            domain = Prompt.ask("Domain (e.g. Fintech, E-commerce, IoT)")
            stmt = Prompt.ask("Problem Description")
            p_a = Prompt.ask("Goal / Metric to Maximize")
            p_b = Prompt.ask("Hard Constraint to Preserve")
            proj = ClientProject(
                client_name=c_name, project_title=p_title, domain=domain,
                problem_statement=stmt, target_metric=p_a, constraint_metric=p_b
            )
            with console.status("[bold cyan]Generating Executive Consulting Report...[/bold cyan]"):
                report = consultant.audit(proj)

    md_content = report.to_markdown()
    console.print("\n")
    console.print(Panel(Markdown(md_content), title="[bold green]Executive Audit Report[/bold green]", border_style="green"))

    out_file = args.out or "triz_consulting_report.md"
    Path(out_file).write_text(md_content, encoding="utf-8")
    console.print(f"\n[bold green]✓ Full report exported to: [underline]{out_file}[/underline][/bold green]")

def cmd_matrix(args):
    console.print(BANNER)
    if args.search:
        results = search_parameters(args.search)
        table = Table(title=f"Parameters matching '{args.search}'")
        table.add_column("#", style="cyan", width=4)
        table.add_column("Classical Name", style="magenta")
        table.add_column("Software / AI Equivalent", style="green")
        table.add_column("Business Equivalent", style="yellow")
        for p in results:
            table.add_row(str(p.id), f"{p.name_en} ({p.name_ru})", p.software, p.business)
        console.print(table)
        return

    if args.improve and args.worsen:
        principles = lookup_principles(args.improve, args.worsen)
        table = Table(title=f"Recommended TRIZ Principles: Parameter #{args.improve} vs #{args.worsen}")
        table.add_column("#", style="cyan", width=4)
        table.add_column("Principle Name", style="bold green")
        table.add_column("Software Mapping", style="magenta")
        table.add_column("Business Mapping", style="yellow")
        for pr in principles:
            table.add_row(str(pr.id), f"{pr.name_en} / {pr.name_ru}", pr.software, pr.business)
        console.print(table)
        return

    # Default: List top software parameters
    table = Table(title="Core TRIZ Engineering Parameters (Sample)")
    table.add_column("#", style="cyan", width=4)
    table.add_column("Classical Name", style="magenta")
    table.add_column("Software / Systems Analog", style="green")
    for i in [9, 1, 27, 36, 14, 19, 32, 33, 30, 39]:
        p = PARAMETERS[i]
        table.add_row(str(p.id), f"{p.name_en} ({p.name_ru})", p.software)
    console.print(table)
    console.print("\n[dim]Usage: triz matrix --improve 9 --worsen 1   (Speed vs Memory)[/dim]")
    console.print("[dim]       triz matrix --search latency[/dim]")

def cmd_serve(args):
    console.print(BANNER)
    import uvicorn
    from triz.web.app import app
    port = args.port or 8000
    console.print(f"[bold green]Starting TRIZ Universal Web UI at http://localhost:{port}[/bold green]")
    uvicorn.run(app, host="127.0.0.1", port=port)

def main():
    parser = argparse.ArgumentParser(description="TRIZ Universal - Open-Source AI Inventive Consultant")
    subparsers = parser.add_subparsers(dest="command")

    # Solve
    p_solve = subparsers.add_parser("solve", help="Solve an architectural or inventive contradiction")
    p_solve.add_argument("--problem", "-p", help="Problem statement")
    p_solve.add_argument("--param-a", "-a", help="Improving parameter")
    p_solve.add_argument("--param-b", "-b", help="Worsening parameter")
    p_solve.add_argument("--passport", action="store_true", help="Always show full Layer 2 TRIZ Passport")
    p_solve.add_argument("--offline", action="store_true", help="Force 100% offline heuristic engine")
    p_solve.add_argument("--out", "-o", help="Save output to markdown file")

    # Consult
    p_consult = subparsers.add_parser("consult", help="Generate a full client consulting report (Side Hustle)")
    p_consult.add_argument("--template", "-t", choices=list(TEMPLATES.keys()), help="Choose a pre-set client archetype")
    p_consult.add_argument("--out", "-o", help="Path to save report markdown")

    # Matrix
    p_matrix = subparsers.add_parser("matrix", help="Lookup or search TRIZ contradiction parameters and principles")
    p_matrix.add_argument("--improve", type=int, help="Parameter ID to improve")
    p_matrix.add_argument("--worsen", type=int, help="Parameter ID that worsens")
    p_matrix.add_argument("--search", "-s", help="Search parameters by keyword")

    # Serve
    p_serve = subparsers.add_parser("serve", help="Launch the Web Dashboard")
    p_serve.add_argument("--port", type=int, default=8000, help="Port to run web server on")

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
