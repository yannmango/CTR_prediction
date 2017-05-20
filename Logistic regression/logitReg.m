function result=logitReg(fileName)
% load 'subset22_hased.norm';
rawData=importdata(fileName);
% testData=importdata('subset99_hased.norm');
% rawData=subset22_hased.norm;
rawData(:,[1,2])=rawData(:,[2,1]);
% testData(:,[1,2])=testData(:,[2,1]);
x=rawData(:,2:end);
y=rawData(:,1);
% test_x=testData(:,2:end);
% test_y=testData(:,1);
% test_x=test_x';
% test_y=test_y';
b=glmfit(x,y,'binomial', 'link', 'logit');
p = glmval(b,x, 'logit');
predict_p=round(p);
score=logLoss(y,p);
result=score;
close all;
end