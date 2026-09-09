# COPILOT-CHEATSHEET.md

## When Things Go Wrong - Quick Fixes

Sometimes Claude Code gets stuck, or Copilot doesn't understand what you need. Here's your troubleshooting cheat sheet.

---

## The Nuclear Option: Reset Everything

When Claude Code or Copilot is confused and won't help:

### Step 1: Right-Click This File
- Right-click on `COPILOT-CHEATSHEET.md` in your explorer
- Select "Copy Path"

### Step 2: Open Copilot Chat
- Press `Cmd+Shift+I` (Mac) or `Ctrl+Shift+I` (Windows)

### Step 3: Paste This

```
I'm having issues with Claude Code / Copilot. Please help me:

1. Read this file: [paste the path you copied]
2. Then help me with my current problem: [describe what's wrong]

If Claude Code has errors or isn't responding, help me clear the session and start fresh.
```

---

## Common Problems & Quick Fixes

### Problem: Claude Code Shows Red Errors
**Quick Fix:**
1. Look at the error message
2. Right-click the error
3. Copy the full error text
4. Paste it into Copilot and ask: "What does this error mean and how do I fix it?"

### Problem: Copilot Won't Understand My Request
**Quick Fix:**
1. Be more specific
2. Instead of: "Help me with this"
3. Try: "I'm working on [project name]. I need to [specific task]. Here's my current code: [paste code]"
4. Always provide context

### Problem: "Claude Code seems stuck"
**Quick Fix:**
1. Close the Claude Code panel (X button)
2. Restart VS Code completely
3. Open a new Claude Code session
4. Try again

### Problem: Extensions Not Working
**Quick Fix:**
1. Command Palette → Search "Extensions: Show Installed"
2. Look for your extension (should have a green checkmark)
3. If not installed, install it
4. Restart VS Code
5. Try again

### Problem: Can't See Rendered Files
**Quick Fix:**
- Markdown not rendering? 
  - Command Palette → "View: Reopen Editor With..."
  - Select "Markdown Preview Enhanced"
- CSV not showing as table?
  - Right-click the file
  - Select "Edit with..." → "Rainbow CSV"
- PDF not opening?
  - Right-click → "Open with..." → "PDF Viewer"

---

## The "Give Me a Hand" Protocol

When you need help from Copilot:

### For Claude Code Issues:
```
My Claude Code is [describe the problem]. 

Can you:
1. Tell me what's wrong
2. Show me the fix
3. Help me prevent this next time
```

### For File Understanding:
```
I don't understand this file. Here's the path: [paste path]

Can you:
1. Read it
2. Explain what it does in simple terms
3. Tell me if there are any errors
```

### For "I'm Stuck":
```
I'm trying to [describe what you want to do].

I've already tried [what you tried].

What should I do next?
```

---

## Keyboard Shortcuts That Save You

| What You Need | Mac | Windows |
|---|---|---|
| Open Copilot Chat | Cmd+Shift+I | Ctrl+Shift+I |
| Command Palette | Cmd+Shift+P | Ctrl+Shift+P |
| Copy Path | Right-click file | Right-click file |
| Search Files | Cmd+P | Ctrl+P |
| Undo | Cmd+Z | Ctrl+Z |
| Zoom In | Cmd+Plus | Ctrl+Plus |
| Zoom Out | Cmd+Minus | Ctrl+Minus |
| Close File | Cmd+W | Ctrl+W |
| Restart VS Code | Close and reopen | Close and reopen |

---

## When to Restart VS Code

✅ **DO restart if:**
- Extensions won't load
- Copilot won't respond
- Files won't render
- You see strange errors
- Claude Code seems frozen

✅ **Steps to restart:**
1. Close VS Code completely
2. Wait 5 seconds
3. Reopen VS Code
4. Usually fixes 80% of problems

---

## The "Fresh Start" Prompt

If everything is broken, copy this into Copilot:

```
I need to reset my VS Code setup. Here's what's happening:
[describe all your problems]

Can you help me:
1. Identify what's broken
2. Fix it step by step
3. Verify everything works
4. Prevent this in the future

My VS Code has these extensions installed:
- GitHub Copilot
- Claude Code
- Markdown Preview Enhanced
- PDF Viewer
- Rainbow CSV
- VSCode Icons
```

---

## Pro Tips

**Tip 1: Always Include Context**
- Don't just say "It doesn't work"
- Say "I'm trying to [task], here's my file [paste], here's the error [paste]"

**Tip 2: Use Copy Path for Everything**
- Stuck on a file? Right-click → Copy Path → Paste into Copilot
- Copilot can read files directly and help better

**Tip 3: Read Error Messages**
- They look scary but they're actually helpful
- Copy the whole error into Copilot
- Copilot will explain it in plain English

**Tip 4: One Problem at a Time**
- Don't ask Copilot to fix 10 things at once
- Describe ONE problem
- Get it fixed
- Move to the next one

**Tip 5: Be Specific About Your Goal**
- Instead of: "Fix this"
- Try: "I want to [specific goal]. Here's what I tried. Here's the error."

---

## Still Stuck?

Follow this order:

1. ✅ **Read the error message** - Copy it to Copilot
2. ✅ **Restart VS Code** - Close and reopen
3. ✅ **Use Copy Path** - Right-click file → Copilot can read it
4. ✅ **Describe your goal** - Tell Copilot what you're trying to do
5. ✅ **Provide context** - Share the file, error, and what you tried

99% of the time, this solves it.

---

## Remember

You're not alone. Copilot is literally there to help you troubleshoot. The better you describe the problem, the better it can help.

**Good description:** "I'm trying to open a CSV file but it shows raw text instead of a table. I have Rainbow CSV installed. Here's the file: [path]"

**Bad description:** "Nothing works"

Copilot can't read minds, but it CAN read files and understand detailed descriptions.

---

**Next Step:** When you're ready, go back to the README and continue with personalization tips, or ask Copilot directly: "I'm stuck. Can you help me?"
