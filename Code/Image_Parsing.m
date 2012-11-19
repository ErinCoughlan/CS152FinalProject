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
finalFileList = cell(0);
[nFiles,nIn]=size(fileList);
for i = 1:nFiles
    fileName = fileList{i};
    
    % split the filenames to get emotions and to compare
    % example:
    % string = 'name_dir_emotion_open.pgm';
    % arr = ['name' 'dir' 'emotion' 'open' 'pgm'];
    arr = regexp(fileName, '_|\.', 'split');
    
    arrDir = arr(DIR);
    arrEmo = arr(EMOTION);
    arrOpen = arr(OPEN);
    
    success = false;
    % We only want to look at pictures that are straight on
    % and don't have glasses
    if strcmp('straight', arrDir) && strcmp('open', arrOpen)
        % initialize hot code
        hotCode = [0 0 0 0];
        success = true;
        if strcmp('angry', arrEmo)
            hotCode(ANGRY) = 1;
        elseif strcmp('happy', arrEmo)
            hotCode(HAPPY) = 1;
        elseif strcmp('neutral', arrEmo)
            hotCode(NEUTRAL) = 1;
        elseif strcmp('sad', arrEmo)
            hotCode(SAD) = 1;
        else
            disp('No emotion data');
            success = false;
        end
    end
    
    if success
        finalFileList = [finalFileList; fileName];
        total = total + 1;
    end
end

face = imread(fileName);
imshow(face);

total

        
