#%%

import matplotlib.pyplot as plt
import numpy as np

security_id = ["TRR-CONF-1","TRR-AUTH-1","TRR-AVAIL-1", "TRR-AUTHOR-1"]
value = [4, 4, 4, 4]
risk_reduction_level = [3, 9, 6, 3]
cost = [3, 2, 2, 1]
colors = ['blue', 'green', 'red', 'purple']
markers = ['o', 'x', '^', 's']
sizes = np.array([3, 3, 4, 5])*50
alpha = [1, 1, 0.5, 0.3]
fontsize = 12
subtitle_fontsize = 14

# Define 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Add one title for all subplots
plt.subplots_adjust(top=0.85, left=0.15) # Adjust top margin to increase padding
fig.suptitle('Risk Prioritisation:', x=0.15, ha='left', fontsize=16)

for i in range(len(security_id)):
    #plt.scatter(risk_reduction_level[i], value[i], color=colors[i], label=security_id[i])

    # Plot risk_reduction_vs value  on first subplot
    axs[0].scatter(risk_reduction_level[i], value[i], color=colors[i], label=security_id[i], s=sizes[i], alpha=alpha[i], marker=markers[i])
    # Plot risk_reduction_vs cost on second subplot
    axs[1].scatter(risk_reduction_level[i], cost[i], color=colors[i], label=security_id[i], s=sizes[i], alpha=alpha[i], marker=markers[i])
    # Plot value vs cost on second subplot
    axs[2].scatter( cost[i], value[i], color=colors[i], label=security_id[i], s=sizes[i], alpha=alpha[i], marker=markers[i])

# Add vertical lines
axs[0].axvline(x=5, color='k', linestyle='--')
axs[1].axvline(x=5, color='k', linestyle='--')
axs[2].axvline(x=1.7, color='k', linestyle='--')

# Add horizontal lines
axs[0].axhline(y=5, color='k', linestyle='--')
axs[1].axhline(y=1.5, color='k', linestyle='--')
axs[2].axhline(y=2.8, color='k', linestyle='--')

# Set axis titles
axs[0].set_title('Risk Reduction Level vs Value', fontsize=subtitle_fontsize)
axs[0].set_xlabel('Risk Reduction Level', fontsize=fontsize)
axs[0].set_ylabel('Value', fontsize=fontsize)

axs[1].set_title('Risk Reduction Level vs Cost', fontsize=subtitle_fontsize)
axs[1].set_xlabel('Risk Reduction Level',fontsize=fontsize)
axs[1].set_ylabel('Cost', fontsize=fontsize)

axs[2].set_title('Cost vs Value', fontsize=subtitle_fontsize)
axs[2].set_xlabel('Cost', fontsize=fontsize)
axs[2].set_ylabel('Value', fontsize=fontsize)

# Set axis limits
axs[0].set_xlim(0, 10)
axs[1].set_xlim(0, 10)
axs[2].set_xlim(0, 10)

axs[0].set_ylim(0, 6)
axs[1].set_ylim(0, 6)
axs[2].set_ylim(0, 6)

plt.legend()
plt.savefig('risk_prioritisation.png')
plt.show()
# %%
