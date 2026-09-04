# Universal AI Coding Assistant Instructions (.github/copilot-instructions.md)

## Standards & Formatting
- **Language:** English for all code, identifiers, commit messages, and documentation. User dialogue adapts to the user's prompt or specified language.
- **Encoding:** Always UTF-8 without BOM.
- **Token Economy & Zero Waste:**
  - Provide direct, concise responses without conversational pleasantries or boilerplate greetings.
  - Maintain a "one task per chat session" discipline (`Ctrl+N`) to preserve full context window capacity.
  - Never dump entire large source files (> 100 lines) into the conversation; provide targeted line edits, diffs, and absolute/relative file paths.
  - Combine multi-step shell commands into a single monolithic block beginning with `clear` (Linux/macOS) or `cls` (Windows).
- **Filesystem Isolation:** Work within dedicated project workspaces; never write temporary artifacts to the user Desktop or system root.