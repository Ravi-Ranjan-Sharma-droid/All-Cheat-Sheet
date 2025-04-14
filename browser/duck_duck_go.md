# DuckDuckGo – Quick Guide for Developers

---

## 1. What is DuckDuckGo?

A **privacy-first** search engine that:
- Doesn’t track you
- Doesn’t store your searches
- Doesn’t profile or target you with ads

Ideal for developers who value **unbiased results**, **security**, and **focus**.

---

## 2. Why Developers Use DuckDuckGo

| Feature              | Benefit to Developers                                                     |
|----------------------|---------------------------------------------------------------------------|
| **Privacy**          | No logs or tracking while researching sensitive or experimental topics   |
| **Neutral Results**  | No personalized ranking—great for unbiased SEO or UI/UX testing          |
| **!Bangs**           | Search directly in dev sites like GitHub, Stack Overflow, MDN, etc.       |
| **Minimal UI**       | Faster, less distracting search environment                               |
| **Open-source Friendly** | Aligns with dev values of transparency and user control              |
| **Fewer Ads**        | Focus on documentation and tools, not product ads                         |
| **Mobile-Friendly**  | Same experience across devices, useful if you switch between phone/laptop |

---

## 3. Powerful !Bang Shortcuts (For Devs)

**Bangs** let you jump directly to other websites from the DuckDuckGo search bar.

| !Bang      | What It Searches                             | Example                          |
|------------|-----------------------------------------------|----------------------------------|
| `!so`      | Stack Overflow                                | `!so javascript async`           |
| `!gh`      | GitHub repositories/issues                    | `!gh react pagination`           |
| `!npm`     | npm package search                            | `!npm axios`                     |
| `!mdn`     | Mozilla Developer Network                     | `!mdn array map`                 |
| `!g`       | Google (when needed)                          | `!g css grid vs flexbox`         |
| `!yt`      | YouTube                                       | `!yt node.js tutorial`           |
| `!devto`   | Dev.to articles                               | `!devto css tricks`              |
| `!reddit`  | Reddit search                                 | `!reddit vscode`                 |
| `!w`       | Wikipedia                                     | `!w linux kernel`                |

> Full list of over **13,000 bangs**: [https://duckduckgo.com/bangs](https://duckduckgo.com/bangs)

---

## 4. Developer Use Cases

| Use Case                            | Why DuckDuckGo Helps                                 |
|-------------------------------------|-------------------------------------------------------|
| Testing SEO/Indexing                | Neutral search results without personalization       |
| Exploring frameworks                | Bangs take you straight to GitHub/npm/MDN            |
| Learning new tech                   | Cleaner results, fewer sponsored distractions        |
| Working on open-source projects     | Privacy-respecting ethos aligns with open-source     |
| Debugging in public Wi-Fi areas     | Pair with VPN + DuckDuckGo for secure access         |

---

## 5. How to Set as Default Search Engine

### Google Chrome / Brave / Edge
1. Go to **Settings → Search Engine**
2. Click **Manage Search Engines**
3. Add DuckDuckGo:
   - Name: DuckDuckGo  
      - Keyword: ddg  
         - URL: `https://duckduckgo.com/?q=%s`
         4. Set as default

         ### Firefox
         - Go to **Settings → Search**
         - Choose DuckDuckGo as your default

         ### VS Code (Optional)
         - Use a *DuckDuckGo Search* extension
         - Or create a custom web search snippet

         ### Android/iOS
         - Set it as default in your browser settings
         - Or install DuckDuckGo’s browser app

         ---

         ## 6. Pro Tips

         - Use `site:` just like in Google:  
           `javascript promises site:stackoverflow.com`

           - Use `filetype:` to find specific file types:  
             `resume template filetype:pdf`

             - Add `!safeoff` to get unrestricted results

             - Use `!duckconfig` to quickly change settings

             - Enable **Dark Mode** in DuckDuckGo settings for night use

             ---