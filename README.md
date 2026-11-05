# graph

**English** · [中文](README.zh-CN.md)

Turn an article, video, paper, report, or dataset into a visual HTML explainer that helps readers understand and explore the source material.

Graph adapts the language, structure, and visual expression to the material. A mechanism may benefit from an interactive comparison; an interview may need to preserve differing viewpoints; a personal account may be best organized around observations and experiences. It preserves important evidence and uncertainty without forcing every subject into the same layout.

## Usage

Install this directory as `graph` in your agent's skill directory, then ask:

```text
Explain this article as a visual page: <URL or text>
Turn this video into a visual guide: <URL or transcript>
Explain this paper's method, results, and limitations: <PDF or link>
Make an explainer from this dataset: <file>
```

The agent needs suitable tools to retrieve or transcribe source material. It should state meaningful gaps in the material it can access.

The page uses interaction when it helps explain the content, keeps visualizations and explanations consistent, and offers light and dark themes when appropriate for interactive reading. It distinguishes source claims, interpretation, teaching assumptions, and uncertainty.

`workflows/` and `references/` provide optional guidance for specific inputs and design problems. `scripts/` contains optional document checks, a browser smoke check, and packaging and preview helpers. Run the helper checks with `python3 -m unittest discover -s tests -v`. Automated checks do not verify factual accuracy or page-specific interaction behavior.

## License

MIT © 2026 ruifengchen
