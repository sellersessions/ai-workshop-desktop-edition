# Copilot Self-Drive File

## How to Use This File

1. **Right-click on this file** in your VS Code explorer
2. **Select "Copy Path"**
3. **Open Copilot Chat** (Cmd+Shift+I / Ctrl+Shift+I)
4. **Paste the path** and ask Copilot to read it:
   ```
   Read this file and help me set up my workspace: [paste path]
   ```
5. **Copilot will guide you through the setup**

---

OR if you prefer:

> Copy everything below and paste it directly into Copilot chat.

---

I'm setting up VS Code with GitHub Copilot for the first time. Copilot's job is to configure my workspace -- install extensions, set up themes, and get everything ready. After this setup, I'll be using Claude Code CLI as my main AI tool.

## My Setup Goals

1. **Install GitHub Copilot** - The AI coding assistant (also my setup tool right now)
2. **Install Claude Code** - The CLI-based AI tool I'll use from Module 1 onwards
3. **Enable Agent Mode** - So Copilot can work autonomously on this setup
4. **Install exactly 6 extensions** - Listed below, no more, no less

## The 6 Extensions to Install

Install these specific extensions by their ID. This is the exact set -- don't add extras:

```
1. github.copilot              GitHub Copilot (setup tool, free tier)
2. github.copilot-chat         Copilot Chat panel
3. anthropic.claude-code       Claude Code (the main AI tool from Module 1)
4. akamud.vscode-theme-onedark One Dark theme
5. cweijan.vscode-office       PDF + WYSIWYG markdown + xlsx viewer
6. yzhang.markdown-all-in-one  Markdown shortcuts + TOC generation
```

## What I Need You To Do

1. **Install all 6 extensions** listed above using their exact IDs
2. **Enable Agent Mode** in Copilot chat (switch the dropdown)
3. **Set the theme** to One Dark (from the extension above)
4. **Verify each extension** is active and working
5. **Tell me when you're done** with a checklist of what was installed

## After Setup

Once all 6 extensions are installed and active:

### Quick Workspace Tweaks
1. Zoom in the font if it feels small: Cmd+Plus (Mac) / Ctrl+Plus (Windows)
2. Pin your project folder in the Explorer sidebar
3. Unpin the Welcome tab
4. Move the sidebar to the right if you prefer: Command Palette -> "Move Primary Sidebar Right"

### Test Everything
1. Open a `.md` file -- should render with formatting
2. Open a `.pdf` file -- should display properly
3. Open a `.csv` or `.xlsx` file -- should show as a table
4. You're ready for Module 1

---

**Next:** Move to Module 1 - Creating your CLAUDE.md (your project's brain)
