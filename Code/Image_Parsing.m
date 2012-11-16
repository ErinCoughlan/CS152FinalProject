% Image Parsing
% Erin Coughlan

string = 'name_dir_emotion_open.pgm';
% split the filenames to get emotions and to compare
% example:
% string = 'name_dir_emotion_open.pgm';
% arr = ['name' 'dir' 'emotion' 'open' 'pgm'];
arr = regexp(string, '_|\.', 'split');