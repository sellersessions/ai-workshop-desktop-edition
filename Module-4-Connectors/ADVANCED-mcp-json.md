# Advanced: the .mcp.json route

Optional. Nothing else in this course needs it.

Connectors are switched on for your account. A file called `.mcp.json` does a similar job for one folder, and it reaches tools that connectors do not, such as browser automation and structured reasoning helpers.

## Read this before you start

This route needs **Node.js** installed on your machine. In the April 2026 version of this course it was the single largest source of problems, so two warnings carry over unchanged:

1. Install Node.js from **nodejs.org**, using the LTS installer for your operating system.
2. **Do not install it with nvm.** nvm puts Node somewhere Claude cannot find, and every tool you add will then fail to start with no useful error.

If you are not comfortable with that, stop here and use connectors. You lose very little.

## What the file looks like

`.mcp.json` sits in the top level of your project folder, beside your `CLAUDE.md`. Each entry is one tool.

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp"]
    }
  }
}
```

On Windows the shape is the same. Only paths inside the arguments differ.

## Adding it

1. Ask Claude to create `.mcp.json` in your project folder with the tools you want. It will write the file for you.
2. Start a new session in that folder.
3. Ask "which tools do you have connected?" and check the new ones are listed.

Testing on 9 September 2026 showed a `.mcp.json` being picked up as soon as the session pointed at the folder, without quitting the app. If your tools do not appear, start a fresh session before assuming anything is broken.

## If a tool does not start

Almost always Node. Confirm Node.js is installed from the nodejs.org installer rather than nvm, then start a new session. If one specific tool still fails, remove it from the file and carry on with the rest. One broken entry does not stop the others.

## The full April package

The original command-line module covers this route in more depth, with six tools and the Windows walkthrough. It is archived in the curriculum repository under `.Archives/2026-04-terminal-edition/Module-4-MCPs/`.
