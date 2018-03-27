from djrulengine.utils import RuleManager


class UserRulesRuleManager(RuleManager):
    code = 'user_rules'

    def initialize_context(self, email, age, country_code, bank_account):
        email_domain = next(iter(email.split('@')[-1:]), '')

        return {
            'email_domain': email_domain,
            'age': age or 0,
            'country_code': country_code,
            'bank_account': bank_account or 0.0
        }
