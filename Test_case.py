import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.analytics_page import AnalyticsPage
from .pages.dion_page import DionPage
from .pages.case_management_page import CaseManagementPage
from .pages.administration_page import AdministrationPage
from .pages.audit_management_page import AuditManagementPage

@pytest.mark.need_run
def test_without_agree(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.set_username("forndldoka7+admin@gmail.com")
    login_page.set_password("1234567Zx!")
    login_page = LoginPage(browser)
    login_page.submit()
    assert login_page.is_error_displayed(), "Error is not displayed"


class TestWithLogin:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_username("forndldoka7+admin@gmail.com")
        login_page.set_password("1234567Zx!")
        login_page.agree_to_terms()
        login_page.submit()

    @pytest.mark.need_run
    def test_with_agree(self, browser):
        main_page = MainPage(browser)
        assert main_page.is_title_displayed(), "Title is not displayed"

    @pytest.mark.need_runw
    def test_main_page(self, browser):
        main_page = MainPage(browser)
        assert main_page.is_analytics_displayed(), "Analytics is not displayed"
        assert main_page.is_dion_displayed(), "Dìon® is not displayed"
        assert main_page.is_case_management_displayed(), "Case management is not displayed"
        assert main_page.is_administration_displayed(), "Administration is not displayed"
        assert main_page.is_audit_management_displayed(), "Audit management is not displayed"

    @pytest.mark.need_run
    def test_analytics(self, browser):
        analytics_page = AnalyticsPage(browser)
        analytics_page.load_analytics()
        assert analytics_page.is_analytics_title_displayed(), "Dashboards list is not displayed"
        assert analytics_page.is_analytics_subscribed_tab_displayed(), "Subscribed tab is not displayed"
        assert analytics_page.is_analytics_dashboard_cards_displayed(), "Dashboard cards is not displayed"

    @pytest.mark.need_run
    def test_dion(self, browser):
        dion_page = DionPage(browser)
        dion_page.load_dion()
        assert dion_page.is_dion_title_displayed(), "ETL DB Configuration is not displayed"
        assert dion_page.is_dion_etl_db_configuration_tab_displayed(), \
            "Health Assessment Dashboard tab is not displayed"

    @pytest.mark.need_run
    def test_case_management(self, browser):
        case_management_page = CaseManagementPage(browser)
        case_management_page.load_case_management()
        assert case_management_page.is_case_management_title_displayed(), "My Cases is not displayed"
        assert case_management_page.is_case_management_participant_displayed(), "PARTICIPANT is not displayed"

    @pytest.mark.need_run
    def test_administration(self, browser):
        administration_page = AdministrationPage(browser)
        administration_page.load_administration()
        assert administration_page.is_administration_title_displayed(), "Title Users is not displayed"
        assert administration_page.is_administration_add_user_button_enabled(), "Add User button is disabled"
        assert administration_page.is_administration_import_user_button_enabled(), "Import User button is disabled"
        assert administration_page.is_administration_force_log_out_button_disabled(), "Force Log Out button is enabled"
        assert administration_page.is_administration_add_user_button_disabled(), "Request Reset Password button is enabled"
        assert administration_page.is_administration_deactivate_button_disabled(), "Deactivate button is enabled"
        assert administration_page.is_administration_users_displayed(), "Table with list of Users is not displayed"

    @pytest.mark.need_run
    def test_audit_management(self, browser):
        audit_management_page = AuditManagementPage(browser)
        audit_management_page.load_audit_management()
        assert audit_management_page.is_audit_management_title_displayed(), "Audit log is not displayed"


