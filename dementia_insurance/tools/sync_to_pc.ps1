<#
用途：把雲端完成的「日本認知症保險盤點」工作搬到本機。
  - 工作資料夾（含 git 倉庫、原始工單、工具）→ C:\ai-work-local\Remote_use
  - 成果資料夾（報告 Word/MD、計畫、工單結果）  → C:\Users\Jack\OneDrive\ai-work\dementia_insurance
執行方式：在 PowerShell 貼上
  powershell -ExecutionPolicy Bypass -File .\sync_to_pc.ps1
需要先安裝 Git for Windows。
#>
param(
  [string]$WorkDir   = "C:\ai-work-local",
  [string]$ResultDir = "C:\Users\Jack\OneDrive\ai-work",
  [string]$Branch    = "claude/japan-dementia-insurance-products-xk7ijh",
  [string]$RepoUrl   = "https://github.com/jackoop-duke/Remote_use.git"
)
$ErrorActionPreference = "Stop"
$repo = Join-Path $WorkDir "Remote_use"
New-Item -ItemType Directory -Force -Path $WorkDir, $ResultDir | Out-Null

if (Test-Path (Join-Path $repo ".git")) {
  Write-Host "已有倉庫，更新中：$repo"
  git -C $repo fetch origin $Branch
  git -C $repo checkout $Branch
  git -C $repo pull origin $Branch
} else {
  Write-Host "下載倉庫到：$repo"
  git clone --branch $Branch $RepoUrl $repo
}

$src  = Join-Path $repo "dementia_insurance"
$dest = Join-Path $ResultDir "dementia_insurance"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Copy-Item (Join-Path $src "report.docx")       $dest -Force
Copy-Item (Join-Path $src "report.md")         $dest -Force
Copy-Item (Join-Path $src "research_plan.md")  $dest -Force
Copy-Item (Join-Path $src "findings")          $dest -Recurse -Force

Write-Host ""
Write-Host "完成。"
Write-Host "  工作資料夾：$repo"
Write-Host "  成果資料夾：$dest"
Get-ChildItem $dest | Select-Object Name, Length, LastWriteTime | Format-Table -AutoSize
