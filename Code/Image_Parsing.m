% Image Parsing
% Erin Coughlan

% set constants for array index
NAME = 1;
DIR = 2;
EMOTION = 3;
OPEN = 4;
EXT = 5;

% set constants for emtions
ANGRY = 1;
HAPPY = 2;
NEUTRAL = 3;
SAD = 4;

dir = strcat(pwd, '/all_images');
fileList = getAllFiles(dir);

total = 0;
[nFiles,nIn]=size(fileList);
for i = 1:nFiles
    fileName = fileList{i};
    % split the filenames to get emotions and to compare
    % example:
    % string = 'name_dir_emotion_open.pgm';
    % arr = ['name' 'dir' 'emotion' 'open' 'pgm'];
    arr = regexp(fileName, '_|\.', 'split');

    % initialize hot code
    hotCode = [0 0 0 0];
    arrEmo = arr(EMOTION);
    if strcmp('angry', arrEmo)
        hotCode(ANGRY) = 1;
        total = total + 1;
    elseif strcmp('happy', arrEmo)
        hotCode(HAPPY) = 1;
        total = total + 1;
    elseif strcmp('neutral', arrEmo)
        hotCode(NEUTRAL) = 1;
        total = total + 1;
    elseif strcmp('sad', arrEmo)
        hotCode(SAD) = 1;
        total = total + 1;
    else
        disp('No emotion data');
    end
end

total

        
