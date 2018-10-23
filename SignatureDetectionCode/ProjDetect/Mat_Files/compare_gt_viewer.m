function compare_gt_viewer()
% this file is used to check the norm of gt_mask/*.png AND
% the masked images using annotation
root = fullfile('F:', 'project');
base_ds = fullfile(root, 'datasets', 'Tobacco800');
gt_mask_base = fullfile(base_ds, 'gt_mask');
images_base = fullfile(base_ds, 'onlysign');

%% save only the filename of signatures wo extension
if ~exist('file.mat', 'file')
    gt_mask_files = dir(gt_mask_base);
    gt_mask_files = {gt_mask_files.name};
    gt_mask_files = {gt_mask_files{3:end}};
    for i=1:length(gt_mask_files)
        gt_mask_files{i} = gt_mask_files{i}(1:end-4);
    end
    save('files.mat', 'gt_mask_files');
end

%% 
if 0
load(fullfile('code', 'ProjDetect', 'Mat_Files', 'files.mat'));
filename = gt_mask_files;
file1 = filename{1};
xml1 = fullfile(annotations_base, [file1, '.xml']);
domData = xml2struct(xml1);
% recursively read .. Children.Name = DT_ZONE and 
% check other attr only when .. Children.Attribute.gedi_type == 'DLSignature'
end

%% load filaname and find box params
load(fullfile('code', 'ProjDetect', 'Mat_Files', 'files.mat'));
filename = gt_mask_files;
stride = 50;
    for fileno = 1: length(filename)
        file1 = filename{fileno};
        image1 = imread(fullfile(images_base, [file1, '.tif']));
        mask1 = imread(fullfile(gt_mask_base, [file1, '.png']));
        [row, col] = find(mask1 == 1);
        minX = min(col); maxX = max(col);
        minY = min(row); maxY = max(row);
        size_mask_box = [maxY - minY, maxX - minX];
        % param for mask box
        X = minX; Y = minY; width = size_mask_box(1); height = size_mask_box(2);

        %hold on
        image12 = image1;        
        %index = sub2ind(size(image1), row, col); % correct
        index_ = 1;
        tID = tic;
        for y = 1:stride:size(image1,1)
            for x = 1:stride:size(image1,2)                          
                if x+stride > size(image1,2)+1
                    x = size(image1,2) - stride + 1;
                end
                if y+stride > size(image1,1)+1
                    y = size(image1,1) - stride + 1;
                end

                cols_patch = int32(x:x+stride-1);
                rows_patch = int32(y:y+stride-1);                        

                % check if the patch overlaps 50% with the signature
                maybe = is_inside([x,y,stride,stride], [X,Y,width,height], file1);                
                patch = image12(rows_patch(:),cols_patch(:));
                
                if ~maybe && sum(patch(:)) == stride*stride % NOT checking for white patches
                    continue;            
                end
                
                % NOT needed for viewer
                %imwrite(patch, fullfile('patches','positive',[file1,'_x' num2str(x),'_y', num2str(y),'.png']));
                
                % viewer
                sz = size(image12);
                imageColor = uint8(zeros(sz(1), sz(2), 3));
                lg_index = image12 == 1;
                imageColor(repmat(lg_index, 1,1,3)) = 255;
                              
                if maybe % is overlapping
                    imageColor(rows_patch(:),cols_patch(:),:) = repmat(reshape([0 255 0], 1, 1,3),stride,stride,1);
                else
                    imageColor(rows_patch(:),cols_patch(:), :) = repmat(reshape([255 0 0], 1, 1,3),stride,stride,1);
                end
                
                %image12(rows_patch(:),cols_patch(:)) = 0;
                imshow(imageColor);
                drawnow;
                index_ = index_ + 1;
                                
                if toc(tID) > 3 
                    disp([num2str(fileno), '/', num2str(length(filename)), '  fname: ', file1]);
                    tID = tic;
                end
            end
        end
    end
    %hold off               
end

function [maybe] = is_inside(patch_, mask_, filename_no_ext)
    maybe = false;
    
    if patch_(1) + patch_(3)/2 >= mask_(1) && ... % LEFT: x center of patch is inside mask rect
       patch_(1) + patch_(3)/2 <= mask_(1)+mask_(4) && ... % RIGHT: x center of patch is inside mask rect
       patch_(2) + patch_(4)/2 >= mask_(2) && ... % LEFT: y center of patch is inside mask rect
       patch_(2) + patch_(4)/2 <= mask_(2)+mask_(3) ... % RIGHT: y center of patch is inside mask rect
    
        maybe = true;   
        
    end
end








