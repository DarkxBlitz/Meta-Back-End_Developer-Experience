    path('', views.home, name="home"),

    path('about/', views.about, name="about"),

    path('book/', views.book, name="book"),

    path('reservations/', views.reservations, name="reservations"),

    path('menu/', views.menu, name="menu"),

    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  

    path('bookings', views.bookings, name='bookings'), 

    path('categories', views.CategoriesView.as_view()),

    path('menu-items', views.MenuItemsView.as_view()),

    path('admin/', admin.site.urls),

    path('', include('restaurant.urls')),

    path('auth/', include('djoser.urls')),

    path('auth/', include('djoser.urls.authtoken')),

    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
