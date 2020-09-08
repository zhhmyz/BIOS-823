---
title: "How I Made this Hugo Site"
date: 2020-08-18T19:17:05-04:00
---

Bascially, I follow the tutorial of Hugo (Quick Start) to set up this website. The website of tutoials I read are https://gohugo.io/hosting-and-deployment/hosting-on-github/
, https://gohugo.io/getting-started/quick-start/

Step 1: Install the Hugo.

```bash
brew install hugo
```

Step 2: Create a new hugo site.

```bash
hugo new site hugo
```

Step 3: Download and install a theme from Github or the official website of Hugo. I chose the theme "ananke"

Step 4: You can start the Hugo server, and add your contents in the file of the /content/posts. The hugo website will automatically change when you change the contents locally. Remember to change the draft to false after you finish editing your contents.

```bash
hugo new posts/my-first-post.md
```

Step 5: Create a new repository in your Github, named it as /user-name/.github.io.Paste your Hugo project to this repository.

Step 6: Create a git submodule to achieve the connection between Hugo and Github.

Step 7: So next time when you want to update the website, you can navigative to the root directory of hugo project. Use command `hugo` to compile your md file to html file. 

Step 8: Push your update to the git repository.



