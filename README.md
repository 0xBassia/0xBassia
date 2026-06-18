<div align="center">

<!-- Custom animated banner -->
<a href="https://github.com/0xBassia"><img src="header.svg" width="100%" alt="Mohamed Bassia, Security Researcher"/></a>

<!-- Typing animation -->
<a href="https://github.com/0xBassia">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=800&color=00FF9C&center=true&vCenter=true&width=640&lines=Security+Researcher+%7C+Vulnerability+Hunter;Source-Code+Auditing+%26+SAST;0-day+Discovery+%26+Responsible+Disclosure;Web+Exploitation+%26+Supply-Chain+Security" alt="Typing SVG"/>
</a>

<br/>

<a href="https://github.com/advisories?query=credit%3A0xBassia"><img src="https://img.shields.io/badge/Focus-Vulnerability%20Research-00ff9c?style=for-the-badge&labelColor=0d1117"/></a>
<a href="https://github.com/advisories?query=credit%3A0xBassia"><img src="https://img.shields.io/badge/Published%20CVEs-10-ff2d78?style=for-the-badge&labelColor=0d1117"/></a>
<a href="https://github.com/0xBassia?tab=followers"><img src="https://img.shields.io/github/followers/0xBassia?style=for-the-badge&color=bd00ff&labelColor=0d1117&label=Followers"/></a>

</div>

---

## `> whoami`

```bash
┌──(root㉿0xbassia)-[~]
└─# cat profile.txt

[+] Name........: Mohamed Bassia
[+] Role........: Security Researcher / Vulnerability Hunter
[+] Specialties.: Source-code auditing, 0-day discovery, web exploitation
[+] Bug classes.: Prototype pollution, SSRF, IDOR, CSRF, auth bypass
[+] Credits.....: 10 published CVEs (6 GitHub-reviewed + 4 WPScan)
[+] Status......: Reading code others trust, finding what they missed
```

## `> arsenal --list`

<div align="center">

**Source-Code Auditing & SAST**

[![CodeQL](https://img.shields.io/badge/CodeQL-2188FF?style=flat-square&logo=github&logoColor=white)](https://codeql.github.com)
[![Semgrep](https://img.shields.io/badge/Semgrep-1B2B34?style=flat-square&logo=semgrep&logoColor=00ff9c)](https://semgrep.dev)
[![CodeChecker](https://img.shields.io/badge/Static%20Analysis-00ff9c?style=flat-square&logo=sonarqube&logoColor=0d1117)](https://www.sonarsource.com)
[![Manual Review](https://img.shields.io/badge/Manual%20Code%20Review-0d1117?style=flat-square&logo=gnometerminal&logoColor=00ff9c)](https://owasp.org/www-project-code-review-guide/)

**Vulnerability Research & Exploitation**

[![Burp Suite](https://img.shields.io/badge/Burp%20Suite%20Pro-FF6633?style=flat-square&logo=burpsuite&logoColor=white)](https://portswigger.net/burp)
[![pwntools](https://img.shields.io/badge/pwntools-0d1117?style=flat-square&logo=python&logoColor=00d4ff)](https://github.com/Gallopsled/pwntools)
[![Ghidra](https://img.shields.io/badge/Ghidra-FF3B30?style=flat-square&logo=ghidra&logoColor=white)](https://ghidra-sre.org)
[![Frida](https://img.shields.io/badge/Frida-E91E63?style=flat-square&logo=frida&logoColor=white)](https://frida.re)

**Fuzzing & Supply-Chain**

[![AFL++](https://img.shields.io/badge/AFL%2B%2B-1B2B34?style=flat-square&logo=gnu&logoColor=00ff9c)](https://github.com/AFLplusplus/AFLplusplus)
[![libFuzzer](https://img.shields.io/badge/libFuzzer-262D3A?style=flat-square&logo=llvm&logoColor=00d4ff)](https://llvm.org/docs/LibFuzzer.html)
[![OSV](https://img.shields.io/badge/OSV%20Scanner-4285F4?style=flat-square&logo=google&logoColor=white)](https://github.com/google/osv-scanner)
[![Dependency Audit](https://img.shields.io/badge/Supply--Chain%20Audit-bd00ff?style=flat-square&logo=npm&logoColor=white)](https://docs.npmjs.com/cli/commands/npm-audit)

**Languages**

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org)
[![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)](https://go.dev)
[![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black)](https://en.cppreference.com/w/c)
[![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)](https://www.gnu.org/software/bash/)

</div>

## `> CVEs --published`

<div align="center">

**10 published CVEs** &nbsp;·&nbsp; **unauth RCE, SSRF, prototype pollution, access control** &nbsp;·&nbsp; npm & WordPress

</div>

| CVE | Package / Plugin | Severity | Vulnerability Class |
|:---|:---|:---:|:---|
| [CVE-2026-47378](https://github.com/advisories/GHSA-4w6r-5c2j-qf5f) | `nocodb` | 🟠 Medium | Hidden column exposure in public shared views (broken access control) |
| [CVE-2026-46510](https://github.com/advisories/GHSA-m2hg-wjq3-28wq) | `form-data-objectizer` | 🔴 High `8.2` | Prototype pollution (bracket-notation keys) |
| [CVE-2026-46509](https://github.com/advisories/GHSA-x7q7-fchv-8h2j) | `@ranfdev/deepobj` | 🔴 High `8.2` | Prototype pollution |
| [CVE-2026-45325](https://github.com/advisories/GHSA-cmxg-94mg-jq94) | `@tmlmobilidade/utils` | 🔴 High `8.2` | Prototype pollution (`setValueAtPath`) |
| [CVE-2026-45302](https://github.com/advisories/GHSA-xp7r-j8r6-j9h3) | `parse-nested-form-data` | 🔴 High `8.2` | Prototype pollution (`__proto__` in form fields) |
| [CVE-2026-44483](https://github.com/advisories/GHSA-c567-44rc-m5hq) | `@rvf/set-get` | 🔴 High `8.2` | Prototype pollution (via `@rvf/core` preprocessFormData) |
| [CVE-2026-9815](https://wpscan.com/vulnerability/043f449f-fc65-4218-83d2-7742e62f2af3) | `MagicForm` (<= 0.1.3) | 🔴 High | Unauthenticated arbitrary file upload to RCE |
| [CVE-2026-12516](https://wpscan.com/vulnerability/2ac80164-03b7-4966-b022-833b4194de80) | `Fediverse Embeds` (< 1.5.8) | 🔴 High `7.5` | Unauthenticated SSRF via media proxy (full read + open proxy) |
| [CVE-2026-12517](https://wpscan.com/vulnerability/460a996f-e27d-47e8-9d68-9e6be93100c0) | `Fediverse Embeds` (< 1.5.8) | 🟠 Medium `5.3` | Unauthenticated SSRF via site-info endpoint |
| [CVE-2026-9067](https://wpscan.com/vulnerability/7fac98eb-f82c-4705-a956-aba650945826) | `Schema & Structured Data for WP & AMP` (< 1.60) | 🔴 High | Unauthenticated arbitrary media upload |

<div align="center">

<sub>6 npm CVEs credited via the <a href="https://github.com/advisories?query=credit%3A0xBassia">GitHub Advisory Database</a> · 4 WordPress CVEs disclosed through <a href="https://wpscan.com/vulnerability/043f449f-fc65-4218-83d2-7742e62f2af3">WPScan</a></sub>

</div>

## `> stats --github`

<div align="center">

<a href="https://github.com/0xBassia"><img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=0xBassia&theme=tokyonight" width="100%" alt="Profile details"/></a>

<a href="https://github.com/0xBassia"><img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=0xBassia&theme=tokyonight"/></a>
<a href="https://github.com/0xBassia"><img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=0xBassia&theme=tokyonight&utcOffset=1"/></a>

<a href="https://github.com/0xBassia"><img src="https://streak-stats.demolab.com?user=0xBassia&disable_animations=true&hide_border=true&background=0d1117&ring=00ff9c&fire=00d4ff&currStreakLabel=00ff9c&sideLabels=8b9cb3&currStreakNum=e6edf3&sideNums=e6edf3&dates=5b6b82" alt="Streak"/></a>

<a href="https://github.com/0xBassia"><img src="https://github-readme-activity-graph.vercel.app/graph?username=0xBassia&bg_color=0d1117&color=8b9cb3&line=00ff9c&point=00d4ff&area=true&area_color=00ff9c&hide_border=true" width="100%" alt="Activity graph"/></a>

</div>

## `> achievements --unlock`

<div align="center">

🛡️ 10× Published CVEs · 🦈 Pull Shark ×2 · ⚡ Quickdraw · 👥 Pair Extraordinaire · 🧊 Arctic Code Vault Contributor

</div>

## `> contact --secure`

<div align="center">

<a href="mailto:0xbassia@gmail.com"><img src="https://img.shields.io/badge/Email-0xbassia@gmail.com-00ff9c?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d1117"/></a>
<a href="https://github.com/0xBassia"><img src="https://img.shields.io/badge/GitHub-0xBassia-00d4ff?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1117"/></a>

<br/><br/>

<a href="https://github.com/0xBassia"><img src="https://komarev.com/ghpvc/?username=0xBassia&style=for-the-badge&color=00ff9c&label=PROFILE+VISITS"/></a>

<br/><br/>

<sub><code>root@0xbassia:~# echo "Hack the planet, responsibly."</code> <code>█</code></sub>

</div>
