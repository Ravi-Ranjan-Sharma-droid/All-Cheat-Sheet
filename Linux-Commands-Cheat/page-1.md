{
  // 🛠️ General Settings — because we pretend to be productive
  "files.autoSave": "afterDelay",
  "editor.mouseWheelZoom": true,
  "editor.cursorBlinking": "expand", // Because blinking cursors are for cowards
  "editor.fontFamily": "Mono Lisa", // She smiles at your syntax
  "editor.fontSize": 18,
  "editor.wordWrap": "on",
  "terminal.integrated.fontSize": 18,
  "editor.minimap.enabled": false, // We don’t need a tiny map, we’re already lost

  // 💾 Formatters — because code should be prettier than our love life
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "editor.formatOnType": true,

  // 📦 Language Specific Formatters
  "[html]": {
    "editor.defaultFormatter": "vscode.html-language-features"
  },
  "[css]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },

  // 🌈 Bracket Madness
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  "editor.guides.bracketPairsHorizontal": "active",
  "editor.guides.highlightActiveBracketPair": true,
  "editor.language.brackets": [],
  "editor.language.colorizedBracketPairs": [],

  // 🎨 The Vibe Section — Dark themes heal wounds
  "workbench.colorTheme": "One Dark Pro Night Flat",
  "workbench.iconTheme": "vscode-icons",

  // 👀 Editor Experience
  "workbench.editor.enablePreview": false,
  "editor.dropIntoEditor.preferences": [],
  "editor.inlineSuggest.enabled": false,
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
  },

  // 🐍 PyMakr Config — for that IoT life
  "pymakr.devices.configs": {
    "562B026976": {
      "autoConnect": "always",
      "name": "",
      "username": "micro",
      "password": "python",
      "hidden": false,
      "rootPath": "/",
      "adapterOptions": {}
    }
  },
  "pymakr.misc.notifications": {
    "A terminal for USB-Enhanced-SERIAL CH9102 (COM3) / unknown already exists.": "No and don't ask again",
    "USB-Enhanced-SERIAL CH9102 (COM3) / unknown seems to be busy. Do you wish restart it in safe mode": "Restart in safe mode",
    "Uploading a project will delete all existing files on the device before uploading the project folder. After uploading a project, you can start it by restarting the device. For faster uploads without file deletion, please put the device in dev mode.": "Don't show again",
    "USB-Enhanced-SERIAL CH9102 (COM3) / Empty Project seems to be busy. Do you wish restart it in safe mode": "Don't show again",
    "A terminal for USB-Enhanced-SERIAL CH9102 (COM3) / Empty Project already exists.": "Create new shared terminal"
  },

  // 🧠 Git Stuff — auto-fetch like a good boi
  "git.autofetch": true,
  "git.openRepositoryInParentFolders": "never",
  "git.suggestSmartCommit": false,

  // 🔥 Live Preview & Server
  "liveServer.settings.donotShowInfoMsg": true,
  "livePreview.hostIP": "192.168.29.94",
  "livePreview.notifyOnOpenLooseFile": false,

  // 🧪 Code Runner
  "code-runner.runInTerminal": true,

  // 🧹 Files & Folders
  "files.exclude": {
    "/.git": false // Because sometimes you *do* want to see the abyss
  },

  // 🧻 Terminal Behavior
  "terminal.integrated.enableMultiLinePasteWarning": "never",
  "terminal.integrated.defaultProfile.windows": "Git Bash"
}
