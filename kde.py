from pandas import np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import LeaveOneOut
from sklearn.neighbors import KernelDensity
import matplotlib.pyplot as plt
import seaborn as sns

def grid(data_frame):
    """bandwidths = 10 ** np.linspace(-1, 1, 100)
    grid = GridSearchCV(KernelDensity(kernel='gaussian'),
                        {'bandwidth': bandwidths},
                        cv=LeaveOneOut())
    #grid.fit([:, None]);
    grid.best_params_"""
    data = data_frame[['latitude','longitude']]
    #data = data_frame.groupby('pls_name')[['latitude', 'longitude']]
    print(data)
    with sns.axes_style('white'):
        #ns.kdeplot(data,bw=1,gridsize=100,n_levels=60)
        #sns.kdeplot("l, "longitude", shade=True)
        sns.jointplot("latitude", "longitude", data, cmap = "Greys",kind='kde');
    plt.show()
    #
    # # use grid search cross-validation to optimize the bandwidth
    # bandwidths = 10 ** np.linspace(-1, 1, 100)
    # # #params = {'bandwidth': np.logspace(-1, 1, 100)}
    # # grid = GridSearchCV(KernelDensity(kernel='gaussian'), {'bandwidth': bandwidths})
    # # grid.fit(data)
    # # print("best bandwidth: {0}".format(grid.best_estimator_.bandwidth))
    #
    # # Set up the data grid for the contour plot
    # X, Y = np.meshgrid(xgrid[::5], ygrid[::5][::-1])
    # land_reference = data.coverages[6][::5, ::5]
    # land_mask = (land_reference > -9999).ravel()
    # xy = np.vstack([Y.ravel(), X.ravel()]).T
    # xy = np.radians(xy[land_mask])

    # # Create two side-by-side plots
    # fig, ax = plt.subplots(1, 2)
    # fig.subplots_adjust(left=0.05, right=0.95, wspace=0.05)
    # species_names = ['Bradypus Variegatus', 'Microryzomys Minutus']
    # cmaps = ['Purples', 'Reds']
    #
    # for i, axi in enumerate(ax):
    #     axi.set_title(species_names[i])
    #
    #     # constr......uct a spherical kernel density estimate of the distribution
    #     kde = KernelDensity(bandwidth=1, metric='haversine')
    #     #kde.fit(np.radians(latlon[species == i]))

        # evaluate only on the land: -9999 indicates ocean
        #Z = np.full(land_mask.shape[0], -9999.0)
        #Z[land_mask] = np.exp(kde.score_samples(xy))
        # #Z = Z.reshape(X.shape)
        #
        # # plot contours of the density
        # levels = np.linspace(0, Z.max(), 25)
        # axi.contourf(X, Y, Z, levels=levels, cmap=cmaps[i])