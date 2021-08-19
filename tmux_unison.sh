#!/bin/zsh

SESSION_NAME="unison"
WINDOW_NAME="unison_notes"

# Check to see if we're already running the session
tmux has-session -t $SESSION_NAME &> /dev/null

if [ $? != 0 ] ; then
    # Create overall tmux session
    tmux new-session -d -s $SESSION_NAME 'unison -auto -repeat 300 -ui text nvAlt_Notes; exec $SHELL'> /dev/null

    # Since we get one window for free on creation, rename it to our scratch windowe
    tmux rename-window -t $SESSION_NAME:0 $WINDOW_NAME
#     tmux send-keys -t $SESSION_NAME:0 "cd /Users;unison_notes" C-m
# 	tmux -c 'cd /Users/kwh;unison_notes'
# 	cd /Users/kwh;unison_notes

else
    echo "tmux session already running, attaching..."
    sleep 2
fi

tmux attach