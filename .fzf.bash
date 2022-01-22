# Setup fzf
# ---------
if [[ ! "$PATH" == */home/dathd6/.fzf/bin* ]]; then
  export PATH="${PATH:+${PATH}:}/home/dathd6/.fzf/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "/home/dathd6/.fzf/shell/completion.bash" 2> /dev/null

# Key bindings
# ------------
source "/home/dathd6/.fzf/shell/key-bindings.bash"
