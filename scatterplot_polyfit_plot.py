# --------------- polyfit scatter  - hs --------------------
pl.figure(figsize=(13,6))
pl.subplot(121)
zpoly=np.polyfit(hs_04[:,0],hs_mod04[:,0],1)
# calculando o histograma de densidade
xy = np.vstack([hs_04[:,0],hs_mod04[:,0]]);z = gaussian_kde(xy)(xy)
pl.scatter(hs_04, hs_mod04, c=z, s=30, vmax=6,vmin=0,edgecolor='')
pl.colorbar();pl.ylim([0,2.5]);pl.xlim([0,2.5])
pl.ylabel('WW3+SWAN Hs (m)',fontsize=12);pl.xlabel('AWAC 04 Hs (m)',fontsize=12)
pl.plot(np.arange(0,3.5,0.1),np.arange(0,3.5,0.1),'k-')
pl.plot(np.arange(0,3.5,0.1),np.arange(0,3.5,0.1)*zpoly[0]+zpoly[1],'k--',linewidth=2.0);pl.grid();
corr_hs = np.corrcoef(hs_mod04[:,0],hs_04[:,0])[0,1] # correlacao
rmse_hs = np.sqrt( pl.sum( (hs_mod04 - hs_04) ** 2 ) / len(hs_04) ) # rmse
si_hs = (rmse_hs / np.mean(hs_04))  #si
bias_hs = np.mean(hs_mod04 - hs_04) # bias
rse04=np.abs([hs_mod04[i,0]-hs_04[i] for i in range(len(hs_mod04))])
me90=np.percentile(rse04,90) # erro 90
N = len(hs_04[:,0])
textstr = '$\mathrm{RMSE}=%.2fm$\n$\mathrm{SI}=%.2f$\n$\mathrm{Bias}=%.2fm$\n$\mathrm{N}=%.0f$'%(rmse_hs, si_hs,bias_hs,N)
#textstr = '$\mathrm{corr}=%.2f$\n$\mathrm{RMSE}=%.2fm$\n$\mathrm{ME90}=%.2fm$\n$\mathrm{SI}=%.2f$\n$\mathrm{Bias}=%.2fm$\n$\mathrm{N}=%.0f$'%(corr_hs, rmse_hs,me90, si_hs,bias_hs,N)
props = dict(boxstyle='round', facecolor='darkgray', alpha=0.5)
pl.text(0.05, 2.4, textstr, fontsize=13,verticalalignment='top', bbox=props)
# ADCP10