import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://akanksha-avy.github.io/Portfolio-QA/"


# PAGE BASICS

def test_page_title(page: Page):
    """Page title should match expected name and role."""
    page.goto(BASE_URL)
    expect(page).to_have_title("Akanksha Yadav — QA Automation Engineer")


def test_page_loads_successfully(page: Page):
    """Page should return HTTP 200 OK."""
    response = page.goto(BASE_URL)
    assert response.status == 200, f"Expected 200 OK but got {response.status}"


def test_page_has_no_console_errors(page: Page):
    """No JavaScript errors should appear on page load."""
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    assert errors == [], f"Console errors found: {errors}"


# NAVIGATION

def test_navbar_is_visible(page: Page):
    """Navbar should be visible on page load."""
    page.goto(BASE_URL)
    expect(page.locator("#navbar")).to_be_visible()


def test_nav_logo_visible(page: Page):
    """Nav logo should always be visible."""
    page.goto(BASE_URL)
    expect(page.locator(".nav-logo")).to_be_visible()


def test_nav_has_five_links(page: Page):
    """Navbar should contain exactly 5 navigation links."""
    page.goto(BASE_URL)
    expect(page.locator(".nav-links a")).to_have_count(5)


def test_nav_links_text(page: Page):
    """Nav link labels should match expected section names exactly."""
    page.goto(BASE_URL)
    expected = ["About", "Skills", "Projects", "AI Testing", "Contact"]
    links = page.locator(".nav-links a").all()
    actual = [link.inner_text() for link in links]
    assert actual == expected, f"Nav links mismatch. Expected {expected}, got {actual}"


def test_nav_about_link_scrolls(page: Page):
    """Clicking About nav link should scroll the About section into view."""
    page.goto(BASE_URL)
    page.locator(".nav-links a[href='#about']").click()
    page.wait_for_timeout(600)
    expect(page.locator("#about")).to_be_in_viewport()


# HERO SECTION

def test_hero_section_visible(page: Page):
    """Hero section should be visible on page load."""
    page.goto(BASE_URL)
    expect(page.locator("#hero")).to_be_visible()


def test_hero_heading_contains_text(page: Page):
    """Hero h1 should contain the core headline text."""
    page.goto(BASE_URL)
    expect(page.locator("#hero h1")).to_contain_text("break things")


def test_hero_cta_buttons_present(page: Page):
    """Hero section should have exactly 2 CTA buttons."""
    page.goto(BASE_URL)
    expect(page.locator(".hero-actions a")).to_have_count(2)


def test_hero_badges_present(page: Page):
    """Hero should display at least 3 skill badges."""
    page.goto(BASE_URL)
    count = page.locator(".hero-badges .badge").count()
    assert count >= 3, f"Expected at least 3 skill badges, found {count}"


# SECTIONS

def test_about_section_visible(page: Page):
    """About section should be present on the page."""
    page.goto(BASE_URL)
    expect(page.locator("#about")).to_be_visible()


def test_skills_section_visible(page: Page):
    """Skills section should be present on the page."""
    page.goto(BASE_URL)
    expect(page.locator("#skills")).to_be_visible()


def test_projects_section_visible(page: Page):
    """Projects section should be present on the page."""
    page.goto(BASE_URL)
    expect(page.locator("#projects")).to_be_visible()


def test_ai_testing_section_visible(page: Page):
    """AI Testing section should be present on the page."""
    page.goto(BASE_URL)
    expect(page.locator("#ai-testing")).to_be_visible()


def test_contact_section_visible(page: Page):
    """Contact section should be present on the page."""
    page.goto(BASE_URL)
    expect(page.locator("#contact")).to_be_visible()


# CONTENT COUNTS

def test_skills_has_six_cards(page: Page):
    """Skills grid should render exactly 6 skill cards."""
    page.goto(BASE_URL)
    expect(page.locator(".skill-card")).to_have_count(6)


def test_ai_section_has_four_cards(page: Page):
    """AI Testing section should render exactly 4 concept cards."""
    page.goto(BASE_URL)
    expect(page.locator(".ai-card")).to_have_count(4)


def test_about_stats_present(page: Page):
    """About section should display at least 3 stat boxes."""
    page.goto(BASE_URL)
    count = page.locator(".stat").count()
    assert count >= 3, f"Expected at least 3 stat boxes, found {count}"


# LINKS & CONTACT

def test_email_link_has_correct_href(page: Page):
    """Contact section should have a valid mailto email link."""
    page.goto(BASE_URL)
    expect(page.locator("#contact a[href^='mailto']")).to_have_count(1)


def test_linkedin_link_present(page: Page):
    """Page should contain a link to LinkedIn profile."""
    page.goto(BASE_URL)
    expect(page.locator("a[href*='linkedin.com']")).to_have_count(1)


def test_github_link_present(page: Page):
    """Page should contain at least one link to GitHub."""
    page.goto(BASE_URL)
    count = page.locator("a[href*='github.com']").count()
    assert count >= 1, "No GitHub link found on page"


# RESPONSIVE

def test_mobile_no_horizontal_scroll(page: Page):
    """Page should not overflow horizontally on mobile (375px viewport)."""
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto(BASE_URL)
    body_width = page.evaluate("document.body.scrollWidth")
    viewport_width = page.evaluate("window.innerWidth")
    assert body_width <= viewport_width + 5, \
        f"Horizontal overflow: body={body_width}px > viewport={viewport_width}px"


def test_tablet_viewport_renders(page: Page):
    """Hero section should be visible on tablet viewport (768px)."""
    page.set_viewport_size({"width": 768, "height": 1024})
    page.goto(BASE_URL)
    expect(page.locator("#hero")).to_be_visible()


def test_desktop_viewport_renders(page: Page):
    """Core sections should be visible on desktop viewport (1280px)."""
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto(BASE_URL)
    expect(page.locator("#hero")).to_be_visible()
    expect(page.locator("#skills")).to_be_visible()
    expect(page.locator("#contact")).to_be_visible()


# FOOTER

def test_footer_visible(page: Page):
    """Footer should be visible at the bottom of the page."""
    page.goto(BASE_URL)
    expect(page.locator("footer")).to_be_visible()


def test_footer_contains_key_text(page: Page):
    """Footer should mention Playwright as part of the brand statement."""
    page.goto(BASE_URL)
    expect(page.locator("footer")).to_contain_text("Playwright")