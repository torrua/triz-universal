"""
FastAPI Web Application for TRIZ Universal.
Provides interactive problem solving, template previews, and consulting report generation.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, List

from triz.engine import OpenSourceAIEngine
from triz.consultant import TEMPLATES, ClientProject, ConsultantSession
from triz.matrix import PRINCIPLES, PARAMETERS, lookup_principles

app = FastAPI(title="TRIZ Universal", description="Open-Source AI Architecture Consultant")
engine = OpenSourceAIEngine()
consultant = ConsultantSession(engine)

class SolveRequest(BaseModel):
    problem: str
    param_a: str = ""
    param_b: str = ""
    offline: bool = False

@app.get("/", response_class=HTMLResponse)
async def index():
    return HTML_CONTENT

@app.get("/api/templates")
async def get_templates():
    return {k: v.model_dump() for k, v in TEMPLATES.items()}

@app.post("/api/solve")
async def solve(req: SolveRequest):
    result = engine.solve(
        problem=req.problem,
        param_a=req.param_a,
        param_b=req.param_b,
        force_offline=req.offline
    )
    return result.model_dump()

@app.get("/api/matrix/lookup")
async def matrix_lookup(improve: int, worsen: int):
    principles = lookup_principles(improve, worsen)
    return [p.__dict__ for p in principles]

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TRIZ Universal — Open-Source AI Architecture Consultant</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    body { background-color: #0b0f19; color: #f3f4f6; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    .glass { background: rgba(23, 31, 48, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.08); }
    .glow-cyan { box-shadow: 0 0 25px rgba(6, 182, 212, 0.2); }
  </style>
</head>
<body class="min-h-screen flex flex-col">

  <!-- Header -->
  <header class="glass border-b border-gray-800 sticky top-0 z-50">
    <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <span class="text-2xl font-black bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">🏛️ TRIZ Universal</span>
        <span class="text-xs uppercase tracking-widest px-2 py-0.5 rounded bg-cyan-950 text-cyan-400 border border-cyan-800 font-mono">Open-Source AI</span>
      </div>
      <div class="flex items-center gap-4 text-sm text-gray-400">
        <span class="inline-flex items-center gap-1.5 text-emerald-400">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> 100% Local / Zero Data Leakage
        </span>
        <a href="https://github.com/torrua/triz-universal" target="_blank" class="hover:text-cyan-400 transition-colors">GitHub</a>
      </div>
    </div>
  </header>

  <!-- Hero -->
  <main class="max-w-6xl mx-auto px-4 py-8 flex-1 w-full space-y-8">
    <div class="text-center space-y-3 max-w-3xl mx-auto">
      <h1 class="text-3xl md:text-5xl font-extrabold tracking-tight">Solve Impossible Trade-Offs Without Compromise</h1>
      <p class="text-gray-400 text-base md:text-lg">
        The Open-Source AI Architectural Consultant for freelancers and solo-founders.
        Implements classical TRIZ (ARIZ-AI) to eliminate contradictions using latent resources with <strong class="text-cyan-300">$0 marginal cost</strong>.
      </p>
    </div>

    <!-- Quick Archetypes -->
    <div class="glass p-4 rounded-xl space-y-3">
      <div class="flex items-center justify-between text-xs text-gray-400 font-mono uppercase tracking-wider">
        <span>⚡ Quick Archetypes (Side Hustle Consulting Cases)</span>
        <span>Click to Load</span>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <button onclick="loadTemplate('freelancer_offline_sync')" class="text-left p-3 rounded-lg bg-gray-900/60 hover:bg-gray-800/80 border border-gray-800 transition-all">
          <div class="font-semibold text-cyan-400 text-sm">📱 Offline Mobile Sync</div>
          <div class="text-xs text-gray-400 mt-1">Instant field editing vs multi-device lock server cost.</div>
        </button>
        <button onclick="loadTemplate('solo_founder_scale')" class="text-left p-3 rounded-lg bg-gray-900/60 hover:bg-gray-800/80 border border-gray-800 transition-all">
          <div class="font-semibold text-blue-400 text-sm">🚀 10k RPS Zero-Cost Scale</div>
          <div class="text-xs text-gray-400 mt-1">Peak viral traffic vs strict $20/month budget ceiling.</div>
        </button>
        <button onclick="loadTemplate('iot_wearable_battery')" class="text-left p-3 rounded-lg bg-gray-900/60 hover:bg-gray-800/80 border border-gray-800 transition-all">
          <div class="font-semibold text-purple-400 text-sm">🔋 IoT Continuous Telemetry</div>
          <div class="text-xs text-gray-400 mt-1">1Hz sensor stream vs 30-day coin-cell battery life.</div>
        </button>
      </div>
    </div>

    <!-- Interactive Form -->
    <div class="glass p-6 rounded-2xl glow-cyan space-y-6">
      <div class="space-y-4">
        <div>
          <label class="block text-sm font-semibold text-gray-300 mb-1">Problem Statement / Technical Deadlock</label>
          <textarea id="problem" rows="3" class="w-full bg-gray-900/80 border border-gray-700 rounded-lg p-3 text-sm text-gray-100 focus:outline-none focus:border-cyan-500 font-mono" placeholder="Describe the architectural conflict, bottleneck, or feature dilemma..."></textarea>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-semibold text-emerald-400 mb-1">Parameter to Maximize (Goal)</label>
            <input type="text" id="param_a" class="w-full bg-gray-900/80 border border-gray-700 rounded-lg p-2.5 text-sm text-gray-100 focus:outline-none focus:border-emerald-500 font-mono" placeholder="e.g. Speed, Scale, Throughput, Accuracy">
          </div>
          <div>
            <label class="block text-sm font-semibold text-rose-400 mb-1">Hard Constraint (Cannot Degrade)</label>
            <input type="text" id="param_b" class="w-full bg-gray-900/80 border border-gray-700 rounded-lg p-2.5 text-sm text-gray-100 focus:outline-none focus:border-rose-500 font-mono" placeholder="e.g. Budget, Memory footprint, Battery, Latency">
          </div>
        </div>
      </div>

      <div class="flex items-center justify-between pt-2">
        <label class="inline-flex items-center gap-2 text-xs text-gray-400 cursor-pointer">
          <input type="checkbox" id="offline_mode" checked class="rounded bg-gray-800 border-gray-700 text-cyan-600 focus:ring-0">
          <span>Deterministic Offline ARIZ Engine (Zero API Key / Instant)</span>
        </label>
        <button onclick="runSolve()" id="solve_btn" class="px-6 py-2.5 rounded-lg bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-semibold text-sm shadow-lg shadow-cyan-500/20 transition-all flex items-center gap-2">
          <span>Resolve Contradiction</span>
          <span>→</span>
        </button>
      </div>
    </div>

    <!-- Output Section -->
    <div id="output_section" class="hidden glass p-6 rounded-2xl space-y-6">
      <div class="flex items-center justify-between border-b border-gray-800 pb-3">
        <div class="flex gap-4">
          <button onclick="switchTab('layer1')" id="tab_layer1" class="font-bold text-sm text-cyan-400 border-b-2 border-cyan-400 pb-2">Layer 1: Plain-Language Core</button>
          <button onclick="switchTab('layer2')" id="tab_layer2" class="font-bold text-sm text-gray-400 hover:text-gray-200 pb-2">Layer 2: Professional TRIZ Passport</button>
          <button onclick="switchTab('vpr')" id="tab_vpr" class="font-bold text-sm text-gray-400 hover:text-gray-200 pb-2">VPR Resource Ledger</button>
        </div>
        <button onclick="copyMarkdown()" class="text-xs bg-gray-800 hover:bg-gray-700 px-3 py-1.5 rounded text-gray-300">Copy Markdown</button>
      </div>

      <div id="view_layer1" class="prose prose-invert max-w-none text-gray-300 text-sm leading-relaxed"></div>
      <div id="view_layer2" class="hidden prose prose-invert max-w-none text-gray-300 text-sm leading-relaxed"></div>
      <div id="view_vpr" class="hidden space-y-4 text-sm"></div>
    </div>
  </main>

  <footer class="glass border-t border-gray-800 py-6 text-center text-xs text-gray-500">
    TRIZ Universal • Built for the DEV Hacktoberfest 2026 Open-Source AI Challenge • Licensed under MIT
  </footer>

  <script>
    let currentResult = null;

    async function loadTemplate(name) {
      const res = await fetch('/api/templates');
      const templates = await res.json();
      const t = templates[name];
      if (t) {
        document.getElementById('problem').value = t.problem_statement;
        document.getElementById('param_a').value = t.target_metric;
        document.getElementById('param_b').value = t.constraint_metric;
      }
    }

    async function runSolve() {
      const btn = document.getElementById('solve_btn');
      btn.disabled = true;
      btn.innerText = "Analyzing ARIZ-AI Pipeline...";

      const payload = {
        problem: document.getElementById('problem').value,
        param_a: document.getElementById('param_a').value,
        param_b: document.getElementById('param_b').value,
        offline: document.getElementById('offline_mode').checked
      };

      try {
        const res = await fetch('/api/solve', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(payload)
        });
        currentResult = await res.json();
        renderResult(currentResult);
      } catch (e) {
        alert("Error executing solution: " + e);
      } finally {
        btn.disabled = false;
        btn.innerHTML = "<span>Resolve Contradiction</span><span>→</span>";
      }
    }

    function renderResult(data) {
      document.getElementById('output_section').classList.remove('hidden');
      document.getElementById('view_layer1').innerHTML = marked.parse(data.layer_1);
      document.getElementById('view_layer2').innerHTML = marked.parse(data.layer_2);

      // Render VPR Ledger
      let vprHtml = '<h3 class="text-base font-bold text-cyan-400">Mobilized Latent Resources (VPR — $0 Cost)</h3>';
      vprHtml += '<div class="overflow-x-auto"><table class="w-full text-left text-xs text-gray-400 border border-gray-800 rounded">';
      vprHtml += '<thead class="bg-gray-900 text-gray-300 font-mono uppercase"><tr><th class="p-2.5">Resource</th><th class="p-2.5">Domain</th><th class="p-2.5">Availability</th><th class="p-2.5">Marginal Cost</th></tr></thead><tbody>';
      for (const r of data.state_lock.mobilized_vpr) {
        vprHtml += `<tr class="border-t border-gray-800/60"><td class="p-2.5 font-bold text-gray-200">${r.name}</td><td class="p-2.5">${r.domain}</td><td class="p-2.5">${r.availability}</td><td class="p-2.5 text-emerald-400">${r.cost}</td></tr>`;
      }
      vprHtml += '</tbody></table></div>';
      document.getElementById('view_vpr').innerHTML = vprHtml;

      switchTab('layer1');
      document.getElementById('output_section').scrollIntoView({behavior: 'smooth'});
    }

    function switchTab(tab) {
      const tabs = ['layer1', 'layer2', 'vpr'];
      for (const t of tabs) {
        document.getElementById(`view_${t}`).classList.add('hidden');
        document.getElementById(`tab_${t}`).classList.remove('text-cyan-400', 'border-b-2', 'border-cyan-400');
        document.getElementById(`tab_${t}`).classList.add('text-gray-400');
      }
      document.getElementById(`view_${tab}`).classList.remove('hidden');
      document.getElementById(`tab_${tab}`).classList.add('text-cyan-400', 'border-b-2', 'border-cyan-400');
      document.getElementById(`tab_${tab}`).classList.remove('text-gray-400');
    }

    function copyMarkdown() {
      if (!currentResult) return;
      const md = currentResult.layer_1 + "\\n\\n---\\n\\n" + currentResult.layer_2;
      navigator.clipboard.writeText(md);
      alert("Copied solution markdown to clipboard!");
    }
  </script>
</body>
</html>
"""
