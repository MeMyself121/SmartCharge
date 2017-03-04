#!/usr/bin/Rscript
series=read.table('serie.txt')
serie=tail(series, floor(length(t(series))/168)*168);
lnserie=log(serie);
ultim=length(lnserie)

(mod=arima(lnserie,order=c(0,1,5),fixed=c(NA,NA,NA,0,0,NA),seasonal=list(order=c(0,1,1),period=7)))

pred=predict(mod,n.ahead=48)
pr<-ts(c(tail(lnserie,1),pred$pred),start=ultim,freq=7)
pr2=exp(as.numeric(pr[2:length(pr)]))
write.table(pr2, file="forecast.txt", row.names=FALSE, col.names=FALSE)
