from django.shortcuts import get_object_or_404, render

from .models import Spell


def list(request):
    spells = Spell.objects.all()
    context = {'spells': spells}
    return render(request, 'spells/spell_list.html', context)


def detail(request, spell_id):
    spell = get_object_or_404(Spell, pk=spell_id)
    return render(request, 'spells/spell_detail.html', {'spell': spell})
