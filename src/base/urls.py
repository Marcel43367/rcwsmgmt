from django.urls import path, include
from base.views import WorkshopListView, WorkshopDetailView, WorkshopFeedbackView, OrderListView, OrderDetailView
from base.views import OrderRedirect, WorkshopPrintBatchListView, WorkshopAnnotateView, WorkshopPrintView
from base.views import WorkshopPrintBatchDownloadView, WorkshopEquivalentUpdateView, WorkshopUpdateView
from base.views import WorkshopListCreateView, WorkshopListListView, WorkshopListDetailView, WorkshopListDeleteView
from base.views import WorkshopAddToListFormView, WorkshopRemoveFromListFormView, WorkshopListDownloadView
from base.views import WorkshopAllDownloadView
urlpatterns = [
    path('', WorkshopListView.as_view(), name="workshop-list"),
    path('workshop/<int:pk>/detail', WorkshopDetailView.as_view(), name='workshop-detail'),
    path('workshop/<int:pk>/addtolist', WorkshopAddToListFormView.as_view(), name='workshop-add-to-list'),
    path('workshop/<int:pk>/removefromlist/<int:wl_pk>', WorkshopRemoveFromListFormView.as_view(), name='workshop-remove-from-list'),
    path('workshop/<int:pk>/eq-update', WorkshopEquivalentUpdateView.as_view(), name='workshop-equivalent'),
    path('workshop/<int:pk>/update', WorkshopUpdateView.as_view(), name='workshop-update'),
    path('workshop/<int:pk>/feedback/<str:template>/<str:next_status>', WorkshopFeedbackView.as_view(), name='workshop-feedback'),
    path('orders', OrderListView.as_view(), name="order-list"),
    path('orders/<int:pk>/detail', OrderDetailView.as_view(), name="order-detail"),
    path('orders/bycode', OrderRedirect.as_view(), name="order-by-code"),
    path('printbatches', WorkshopPrintBatchListView.as_view(), name="printbatch-list"),
    path('printbatches/annotate', WorkshopAnnotateView.as_view(), name="printbatch-annotate"),
    path('printbatches/create', WorkshopPrintView.as_view(), name="printbatch-create"),
    path('printbatches/<int:pk>/download', WorkshopPrintBatchDownloadView.as_view(), name="printbatch-download"),
    path('printbatches/all/download', WorkshopAllDownloadView.as_view(), name="all-ws-download"),
    path('lists/create', WorkshopListCreateView.as_view(), name='workshoplist-create'),
    path('lists', WorkshopListListView.as_view(), name='workshoplist-list'),
    path('lists/<int:pk>', WorkshopListDetailView.as_view(), name='workshoplist-detail'),
    path('lists/<int:pk>/delete', WorkshopListDeleteView.as_view(), name='workshoplist-delete'),
    path('lists/<int:pk>/download', WorkshopListDownloadView.as_view(), name='workshoplist-download'),
]

