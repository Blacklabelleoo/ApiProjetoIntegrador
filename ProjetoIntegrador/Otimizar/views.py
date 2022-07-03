from rest_framework import viewsets, generics
from Otimizar.models import Peca, Sobra, Aproveita
from Otimizar.serializer import PecaSerializer, SobraSerializer, AproveitaSerializer, ListaAproveitaSobraSerializer

class PecasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Pecas"""
    queryset = Peca.objects.all() #aqui talvez vai ser o filtro da peca e tals
    serializer_class = PecaSerializer

class SobrasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as sobras"""
    queryset = Sobra.objects.all() #aqui talvez vai ser o filtro da peca e tals
    serializer_class = SobraSerializer

class AproveitaViewSet(viewsets.ModelViewSet):
    """Exibindo os aproveitamentos"""
    queryset = Aproveita.objects.all()
    serializer_class = AproveitaSerializer

class ListaAproveitaSobra(generics.ListAPIView):
    """Listando as sobras para essa peça"""
    def get_queryset(self):
        queryset = Aproveita.objects.filter(peca_id = self.kwargs['pk'])
        return queryset

    serializer_class = ListaAproveitaSobraSerializer