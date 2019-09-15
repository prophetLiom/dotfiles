if empty(glob('~/.vim/autoload/plug.vim'))
	silent !curl -flo ~/.vim/autoload/plug.vim --create-dirs
				\ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
	autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

set number
map <C-o> :NERDTreeToggle<CR> 
map <C-r> :! clear; python %<CR>
map <tab> <C-w>w

call plug#begin('~/.vim/plugged')
Plug 'scrooloose/nerdtree', {'on': 'NERDTreeToggle'}
Plug 'morhetz/gruvbox'
Plug 'itchyny/lightline.vim'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'makerj/vim-pdf'
Plug 'dylanaraps/wal.vim'

call plug#end()


colorscheme wal



autocmd VimEnter * NERDTreeToggle

