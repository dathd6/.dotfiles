syntax on
set path+=**
set wildmode=longest,list,full
set wildmenu
set hidden
" Ignore files
set wildignore+=*.pyc
set wildignore+=*_build/*
set wildignore+=**/coverage/*
set wildignore+=**/node_modules/*
set wildignore+=**/android/*
set wildignore+=**/ios/*
set wildignore+=**/.git/*
set number
set relativenumber
" Spaces & Tabs {{{
set tabstop=4       " number of visual spaces per TAB
set softtabstop=4   " number of spaces in tab when editing
set shiftwidth=4    " number of spaces to use for autoindent
set expandtab       " tabs are space
set autoindent
set copyindent      " copy indent from the previous line
" }}} Spaces & Tabs

call plug#begin()
    " Neovim lsp Plugins
    Plug 'neovim/nvim-lspconfig'
    Plug 'hrsh7th/cmp-nvim-lsp'
    Plug 'hrsh7th/cmp-buffer'
    Plug 'hrsh7th/nvim-cmp'
    Plug 'tzachar/cmp-tabnine', { 'do': './install.sh' }
    Plug 'onsails/lspkind-nvim'

	Plug 'neoclide/coc.nvim', {'branch': 'release'}
	Plug 'tjdevries/colorbuddy.vim'
    Plug 'tjdevries/gruvbuddy.nvim'

    Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
    Plug 'nvim-treesitter/playground'

	Plug 'p00f/nvim-ts-rainbow'

    Plug 'nvim-lua/popup.nvim'
	Plug 'nvim-lua/plenary.nvim'
	Plug 'nvim-telescope/telescope.nvim'
	Plug 'nvim-telescope/telescope-fzy-native.nvim'

	Plug 'norcalli/nvim-colorizer.lua'
"	Plug 'lukas-reineke/indent-blankline.nvim'
	Plug 'windwp/nvim-autopairs'
	Plug 'neoclide/coc-prettier'
	Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'

	Plug 'christoomey/vim-tmux-navigator'

	Plug 'preservim/nerdtree'
	Plug 'Xuyuanp/nerdtree-git-plugin'
	Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
	Plug 'ryanoasis/vim-devicons'
"
	Plug 'morhetz/gruvbox'

"    Copy to system clipboard
    Plug 'christoomey/vim-system-copy'

call plug#end()

" Adding local modules
""let &runtimepath.=',' . expand("$HOME") . '/personal/harpoon/tmux'
""let &runtimepath.=',' . expand("$HOME") . '/personal/vim-with-me/ui'
""let &runtimepath.=',' . expand("$HOME") . '/personal/git-worktree.nvim/master'
""let &runtimepath.=',' . expand("$HOME") . '/personal/refactoring.nvim/master'

lua require("dathd")

""""" Add python LSP
lua << EOF
    require 'lspconfig'.pyright.setup{}
    require 'lspconfig'.tsserver.setup{}
EOF
"""""

""""" Support LSP snippets

"""""""""""""""""""""""""""

""""" Color Scheme
colorscheme gruvbox
highlight Normal guibg=none guifg=none
"""" Module Treesitter

lua <<EOF
    require'nvim-treesitter.configs'.setup {
      highlight = {
        enable = true,
        custom_captures = {
          -- Highlight the @foo.bar capture group with the "Identifier" highlight group.
          ["foo.bar"] = "Identifier",
        },
        -- Setting this to true will run `:h syntax` and tree-sitter at the same time.
        -- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
        -- Using this option may slow down your editor, and you may see some duplicate highlights.
        -- Instead of true it can also be a list of languages
        additional_vim_regex_highlighting = false,
      },
      incremental_selection = {
        enable = true,
        keymaps = {
          init_selection = "gnn",
          node_incremental = "grn",
          scope_incremental = "grc",
          node_decremental = "grm",
        },
      },
      rainbow = {
        enable = true,
        -- disable = { "jsx", "cpp" }, list of languages you want to disable the plugin for
        extended_mode = true, -- Also highlight non-bracket delimiters like html tags, boolean or table: lang -> boolean
        max_file_lines = nil, -- Do not enable for files with more than n lines, int
        -- colors = {}, -- table of hex strings
        -- termcolors = {} -- table of colour name strings
      },
      indent = {
          enable = true
      },
      playground = {
          enable = true,
          disable = {},
          updatetime = 25, -- Debounced time for highlighting nodes in the playground from source code
          persist_queries = false, -- Whether the query persists across vim sessions
          keybindings = {
            toggle_query_editor = 'o',
            toggle_hl_groups = 'i',
            toggle_injected_languages = 't',
            toggle_anonymous_nodes = 'a',
            toggle_language_display = 'I',
            focus_language = 'f',
            unfocus_language = 'F',
            update = 'R',
            goto_node = '<cr>',
            show_help = '?',
          },
      },
      query_linter = {
          enable = true,
          use_virtual_text = true,
          lint_events = {"BufWrite", "CursorHold"},
      }
    }
EOF

hi rainbowcol1 guifg=#616a78

""" colorizer
"lua require'colorizer'.setup()
"""

""" nvim auto pair
lua <<EOF
    require('nvim-autopairs').setup({
        disable_filetype = { "TelescopePrompt" , "vim" },
    })
EOF

let g:coc_global_extensions = [
    \ 'coc-snippets',
    \ 'coc-pairs',
    \ 'coc-eslint',
    \ 'coc-prettier',
    \ 'coc-json',
    \ 'coc-tsserver',
    \ 'coc-pyright',
    \ ]

let g:NERDTreeIgnore = ['^node_modules$']
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTreeToggle<CR>
nnoremap <C-x> :NERDTreeFind<CR>

let g:NERDTreeGitStatusIndicatorMapCustom = {
    \ 'Modified'  :'✹',
    \ 'Staged'    :'✚',
    \ 'Untracked' :'✭',
    \ 'Renamed'   :'➜',
    \ 'Unmerged'  :'═',
    \ 'Deleted'   :'✖',
    \ 'Dirty'     :'✗',
    \ 'Ignored'   :'☒',
    \ 'Clean'     :'✔︎',
    \ 'Unknown'   :'?',
    \ }


"let g:tmux_navigator_no_mappings = 1

"nnoremap <silent> {Left-Mapping} :TmuxNavigateLeft<cr>
"nnoremap <silent> {Down-Mapping} :TmuxNavigateDown<cr>
"nnoremap <silent> {Up-Mapping} :TmuxNavigateUp<cr>
"nnoremap <silent> {Right-Mapping} :TmuxNavigateRight<cr>
"nnoremap <silent> {Previous-Mapping} :TmuxNavigatePrevious<cr>
"
if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
  endif
  "For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
  "Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
  " < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >
  if (has("termguicolors"))
    set termguicolors
  endif
