Sublime Text 2 MarkDown preview - Tumblr Fork
=====

A simple ST2 plugin to help you preview your markdown files, and send them to Tumblr.

**Installation :**

 - Clone the repository
 ``` shell
 git clone https://github.com/blakeanderson/sublimetext-markdown-preview.git MarkdownPreview
 ```
 - Place the plugin in your Sublime Text 2 `Packages` directory

  - OS X: `~/Library/Application Support/Sublime Text 2/Packages/`
  - Windows: `%APPDATA%/Sublime Text 2/Packages/`
  - Linux: `~/.Sublime Text 2/Packages/`

**Settings :**
  
  For the plugin to work, you will need to update MarkdownPreview.sublime-settings

  Add your Tumblr username and password.

  `MarkdownPreview.sublime-settings`

  	{
  		// Tumblr Username
  		"email": "", 

  		// Tumblr Password
  		"password": "",
  	}

**Usage :**

 - use `cmd+shift+P` then `MarkdownPreview: publish current file to Tumblr` to send the current file to Tumblr and mark it as published
 - use `cmd+shift+P` then `MarkdownPreview: send current file to Tumblr as a draft` to launch send the current file to Tumblr as a draft

**Uses :**

 - [python-markdown][0] for markdown parsing
 - [clownfart markown.css][1] for markdown styling

The tumblr fork code is available at github [https://github.com/blakeanderson/sublimetext-markdown-preview][2]

Licence MIT : [http://revolunet.mit-license.org][4]

 [0]: https://github.com/waylan/Python-Markdown
 [1]: https://github.com/clownfart/Markdown-CSS
 [2]: https://github.com/revolunet/sublimetext-markdown-preview
 [3]: http://wbond.net/sublime_packages/package_control
 [4]: http://revolunet.mit-license.org
