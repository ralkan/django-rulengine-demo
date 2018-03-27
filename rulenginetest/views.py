from django.http import HttpResponse
from .rules import UserRulesRuleManager
from .forms import RulengineForm


def test_view(request):
    form = RulengineForm(data=request.GET)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        rule_manager = UserRulesRuleManager(cleaned_data['email'],
                                            cleaned_data['age'],
                                            cleaned_data['country'],
                                            cleaned_data['bank_account'])
        result = rule_manager.execute()

        if result:
            return HttpResponse('TRUE')

        return HttpResponse(
            'email: {}<br />'.format(cleaned_data['email']) +
            'age: {}<br />'.format(cleaned_data['age'] or 0) +
            'country: {}<br />'.format(cleaned_data['country']) +
            'bank_account: {}<br />'.format(
                cleaned_data['bank_account'] or 0) +
            '<br />'
            'Rules resulted to: {}'.format(str(result))
        )
    return HttpResponse('Parameters are invalid')
