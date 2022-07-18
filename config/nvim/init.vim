let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
set termguicolors
set number
set clipboard^=unnamed,unnamedplus
set noshowmode
set noshowcmd
let g:nord_italic = v:false

call plug#begin('~/.config/nvim/plugged')
Plug 'shaunsingh/nord.nvim'
Plug 'nvim-lualine/lualine.nvim'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'github/copilot.vim'
call plug#end()

lua << END
require'lualine'.setup {
  options = {
    icons_enabled = true,
    theme = 'nord_new',
    component_separators = { right = '|'}, -- Experimental separator: ' ⃒'
    -- default: component_separators = { left = '', right = ''}, 
    section_separators = { left = '', right = ''},
    -- default: section_separators = { left = '', right = ''},
    disabled_filetypes = {},
    always_divide_middle = false,
  },
  sections = {
    lualine_a = {{ 'mode', separator = { left = '', right = ''}}},
    lualine_b = {'branch'},
    lualine_c = {{'filename', file_status = true, path = 0}}, 
    lualine_x = {'fileformat', 'filetype'},
    lualine_y = {'%L'},
    lualine_z = {{ 'location', separator = { left = '', right = ''}}},
    },
  inactive_sections = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {'filename'},
    lualine_x = {'location'},
    lualine_y = {},
    lualine_z = {}
  },
  tabline = {},
  extensions = {}
}

require'nvim-web-devicons'.setup {
 -- you can specify color or cterm_color instead of specifying both of them
 -- DevIcon will be appended to `name`
 override = {
  py = {
    icon = "",
    color = "#3777ac",
    --cterm_color = "67",
    name = "py"
  }
 };
 -- globally enable default icons (default to false)
 -- will get overriden by `get_icons` option
 default = true;
}

require'nvim-treesitter.configs'.setup {
  -- One of "all", "maintained" (parsers with maintainers), or a list of languages
  --ensure_installed = "maintained",

  -- Install languages synchronously (only applied to `ensure_installed`)
  --sync_install = false,

  -- List of parsers to ignore installing
  --ignore_install = { "javascript" },

  highlight = {
    -- `false` will disable the whole extension
    enable = true,

    -- list of language that will be disabled
    disable = { },

    -- Setting this to true will run `:h syntax` and tree-sitter at the same time.
    -- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
    -- Using this option may slow down your editor, and you may see some duplicate highlights.
    -- Instead of true it can also be a list of languages
    additional_vim_regex_highlighting = false,
  },
}
END

colorscheme nord
