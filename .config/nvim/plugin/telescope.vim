lua require("dathd")

nnoremap <C-f> :lua require('telescope.builtin').grep_string({ search = vim.fn.input("Grep For > ")})<CR>
nnoremap <leader>pf :lua require('telescope.builtin').git_files()<CR>
nnoremap <C-p> :lua require('telescope.builtin').find_files()<CR>

nnoremap <leader>pw :lua require('telescope.builtin').grep_string { search = vim.fn.expand("<cword>") }<CR>

"nnoremap <leader>pb :lua require('telescope.builtin').buffers()<CR>
"nnoremap <leader>vh :lua require('telescope.builtin').help_tags()<CR>
"nnoremap <leader>vrc :lua require('dathd.telescope').search_dotfiles({ hidden = true })<CR>
"nnoremap <leader>va :lua require('dathd.telescope').anime_selector()<CR>
"nnoremap <leader>vc :lua require('dathd.telescope').chat_selector()<CR>
"nnoremap <leader>gc :lua require('dathd.telescope').git_branches()<CR>
"nnoremap <leader>gw :lua require('telescope').extensions.git_worktree.git_worktrees()<CR>
"nnoremap <leader>gm :lua require('telescope').extensions.git_worktree.create_git_worktree()<CR>
"nnoremap <leader>td :lua require('dathd.telescope').dev()<CR>
