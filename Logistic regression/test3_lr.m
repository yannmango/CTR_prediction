clear;close all;
tic
name={'subset5_hased.norm','subset6_hased.norm','subset9_hased.norm','subset13_hased.norm','subset16_hased.norm','subset19_hased.norm','subset21_hased.norm','subset22_hased.norm'};

resource=[];
[width,length]=size(name);
for i=1:length
    rawData=importdata(name{i});
    resource=[resource;rawData];
end
test=importdata('subset99_hased.norm');
test(:,[1,2])=test(:,[2,1]);
test_x=test(:,2:end);
test_y=test(:,1);
resource(:,[1,2])=resource(:,[2,1]);
x=resource(:,2:end);
y=resource(:,1);
b=glmfit(x,y,'binomial', 'link', 'logit');
p2=glmval(b,x, 'logit');
p = glmval(b,test_x, 'logit');
predict_p=round(p);
score=logLoss(test_y,p);
score2=logLoss(y,p2);
result=FMeasure(test_y,predict_p);
toc
close all;