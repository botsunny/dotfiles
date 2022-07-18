Dotfiles for KDE Plasma, Qtile, and a bunch of other applications I use, all Nord-themed.
Managed with [Dotdrop](https://github.com/deadc0de6/dotdrop). You can ignore `config.yaml` in the root directory if you are not using Dotdrop.

For line 21 of `init.vim`, due to unknown theme conflicts, the setting `theme = 'nord'` does not work properly for Lualine. The Nord colours may be incorrect. This is fixed by adding the provided `nord_new.lua` to `[your_vim-plug_path]/lualine.nvim/lua/lualine/themes`, and setting `theme = nord_new`.
