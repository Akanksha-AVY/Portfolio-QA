import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://akanksha-avy.github.io/Portfolio-QA/"


# ============================================================
# PAGE BASICS
# ============================================================

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


def test_page_has_meta_viewport(page: Page):
    """Page should have a meta viewport tag for mobile responsiveness."""
    page.goto(BASE_URL)
    viewport = page.locator("meta[name='viewport']")
    expect(viewport).to_have_count(1)


def test_page_has_meta_charset(page: Page):
    """Page should declare UTF-8 charset."""
    page.goto(BASE_URL)
    charset = page.locator("meta[charset]")
    expect(charset).to_have_count(1)


# ============================================================
# NAVIGATION
# ============================================================

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


def test_nav_contact_link_scrolls(page: Page):
    """Clicking Contact nav link should scroll the Contact section into view."""
    page.goto(BASE_URL)
    page.locator(".nav-links a[href='#contact']").click()
    page.wait_for_timeout(600)
    expect(page.locator("#contact")).to_be_in_viewport()


def test_nav_skills_link_scrolls(page: Page):
    """Clicking Skills nav link should scroll the Skills section into view."""
    page.goto(BASE_URL)
    page.locator(".nav-links a[href='#skills']").click()
    page.wait_for_timeout(600)
    expect(page.locator("#skills")).to_be_in_viewport()


# ============================================================
# HERO SECTION
# ============================================================

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


def test_hero_see_my_work_button(page: Page):
    """'See My Work' CTA should link to #projects section."""
    page.goto(BASE_URL)
    btn = page.locator(".hero-actions a[href='#projects']")
    expect(btn).to_be_visible()
    expect(btn).to_contain_text("See My Work")


def test_hero_get_in_touch_button(page: Page):
    """'Get In Touch' CTA should link to #contact section."""
    page.goto(BASE_URL)
    btn = page.locator(".hero-actions a[href='#contact']")
    expect(btn).to_be_visible()
    expect(btn).to_contain_text("Get In Touch")


def test_hero_badges_present(page: Page):
    """Hero should display at least 3 skill badges."""
    page.goto(BASE_URL)
    count = page.locator(".hero-badges .badge").count()
    assert count >= 3, f"Expected at least 3 skill badges, found {count}"


def test_hero_tag_contains_istqb(page: Page):
    """Hero tag should mention ISTQB certification."""
    page.goto(BASE_URL)
    expect(page.locator(".hero-tag")).to_contain_text("ISTQB")


# ============================================================
# SECTIONS
# ============================================================

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


# ============================================================
# CONTENT COUNTS
# ============================================================

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


def test_about_stats_have_content(page: Page):
    """Each stat box should contain a number and a label."""
    page.goto(BASE_URL)
    stat_nums = page.locator(".stat-num").all()
    for num in stat_nums:
        assert num.inner_text().strip() != "", "Stat number should not be empty"


def test_projects_section_has_two_cards(page: Page):
    """Projects section should display exactly 2 project cards."""
    page.goto(BASE_URL)
    expect(page.locator(".project-card")).to_have_count(2)


def test_featured_project_card_exists(page: Page):
    """There should be exactly one featured project card."""
    page.goto(BASE_URL)
    expect(page.locator(".project-card.featured")).to_have_count(1)


def test_ai_cards_have_numbered_labels(page: Page):
    """Each AI card should have a numbered label (01-04)."""
    page.goto(BASE_URL)
    ai_nums = page.locator(".ai-num").all()
    expected = ["01", "02", "03", "04"]
    actual = [n.inner_text().strip() for n in ai_nums]
    assert actual == expected, f"AI card numbers mismatch: expected {expected}, got {actual}"


# ============================================================
# LINKS & CONTACT
# ============================================================

def test_email_link_has_correct_href(page: Page):
    """Contact section should have a valid mailto email link."""
    page.goto(BASE_URL)
    expect(page.locator("#contact a[href^='mailto']")).to_have_count(1)


def test_email_link_correct_address(page: Page):
    """Email link should point to the correct email address."""
    page.goto(BASE_URL)
    email_link = page.locator("#contact a[href^='mailto']")
    href = email_link.get_attribute("href")
    assert "akanksha" in href.lower(), f"Email href unexpected: {href}"


def test_linkedin_link_present(page: Page):
    """Page should contain a link to LinkedIn profile."""
    page.goto(BASE_URL)
    expect(page.locator("a[href*='linkedin.com']")).to_have_count(1)


def test_linkedin_link_correct_profile(page: Page):
    """LinkedIn link should point to Akanksha's profile specifically."""
    page.goto(BASE_URL)
    linkedin = page.locator("a[href*='linkedin.com']")
    href = linkedin.get_attribute("href")
    assert "akanksha-yadav04" in href, f"LinkedIn URL unexpected: {href}"


def test_github_link_present(page: Page):
    """Page should contain at least one link to GitHub."""
    page.goto(BASE_URL)
    count = page.locator("a[href*='github.com']").count()
    assert count >= 1, "No GitHub link found on page"


def test_github_project_link_correct(page: Page):
    """Portfolio QA project should link to the correct GitHub repo (Portfolio-QA)."""
    page.goto(BASE_URL)
    link = page.locator("a[href*='Portfolio-QA']")
    expect(link).to_have_count(1)


def test_test_report_link_present(page: Page):
    """'View Test Report' button should be visible in the Projects section."""
    page.goto(BASE_URL)
    report_link = page.locator("#test-report-link")
    expect(report_link).to_be_visible()


def test_test_report_link_opens_new_tab(page: Page):
    """'View Test Report' button should open in a new tab."""
    page.goto(BASE_URL)
    report_link = page.locator("#test-report-link")
    target = report_link.get_attribute("target")
    assert target == "_blank", f"Expected target='_blank', got '{target}'"


# ============================================================
# BUG: INCONSISTENT NAME SPELLING
# This is a known issue — nav logo says "Aakanksha" (double A)
# but About section and page title say "Akanksha" (single A).
# These tests document the inconsistency.
# ============================================================

def test_page_title_name_spelling(page: Page):
    """Page title should use 'Akanksha' (single A) spelling."""
    page.goto(BASE_URL)
    title = page.title()
    assert "Akanksha" in title, f"Expected 'Akanksha' in title, got: {title}"


def test_about_section_name_spelling(page: Page):
    """About section should use 'Akanksha' (single A) spelling."""
    page.goto(BASE_URL)
    about_text = page.locator("#about").inner_text()
    assert "Akanksha" in about_text, "Expected 'Akanksha' in About section"


def test_nav_logo_name_spelling(page: Page):
    """BUG: Nav logo uses 'Aakanksha' (double A) — inconsistent with rest of site."""
    page.goto(BASE_URL)
    logo_text = page.locator(".nav-logo").inner_text()
    # This test intentionally FAILS to document the inconsistency
    assert logo_text == "Akanksha", f"Name inconsistency: nav logo shows '{logo_text}' but should match 'Akanksha'"


# ============================================================
# BUG: GITHUB LINK IN PROJECTS SECTION
# The "GitHub →" link under Portfolio QA project points to
# github.com/akanksha-yadav04 (wrong — no -AVY suffix)
# instead of github.com/Akanksha-AVY (correct profile)
# ============================================================

def test_portfolio_github_link_correct(page: Page):
    """BUG: Portfolio project GitHub link should point to correct profile (Akanksha-AVY)."""
    page.goto(BASE_URL)
    # Find the GitHub link in the featured project card specifically
    github_link = page.locator(".project-card.featured a[href*='github.com']")
    href = github_link.get_attribute("href")
    # This test intentionally FAILS to document the wrong URL
    assert "Akanksha-AVY" in href, f"BUG: GitHub link points to '{href}' — should be 'Akanksha-AVY'"


# ============================================================
# RESPONSIVE
# ============================================================

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


def test_large_desktop_viewport(page: Page):
    """Site should render correctly on large desktop (1920px)."""
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(BASE_URL)
    expect(page.locator("#hero")).to_be_visible()
    expect(page.locator("#navbar")).to_be_visible()


def test_small_mobile_viewport(page: Page):
    """Site should render on small mobile (320px) without breaking."""
    page.set_viewport_size({"width": 320, "height": 568})
    page.goto(BASE_URL)
    expect(page.locator("#hero")).to_be_visible()
    body_width = page.evaluate("document.body.scrollWidth")
    viewport_width = page.evaluate("window.innerWidth")
    assert body_width <= viewport_width + 5, \
        f"Overflow on 320px: body={body_width}px > viewport={viewport_width}px"


# ============================================================
# FOOTER
# ============================================================

def test_footer_visible(page: Page):
    """Footer should be visible at the bottom of the page."""
    page.goto(BASE_URL)
    expect(page.locator("footer")).to_be_visible()


def test_footer_contains_playwright(page: Page):
    """Footer should mention Playwright as part of the brand statement."""
    page.goto(BASE_URL)
    expect(page.locator("footer")).to_contain_text("Playwright")


def test_footer_contains_github_actions(page: Page):
    """Footer should mention GitHub Actions."""
    page.goto(BASE_URL)
    expect(page.locator("footer")).to_contain_text("GitHub Actions")


def test_footer_contains_author_name(page: Page):
    """Footer should contain the author's name."""
    page.goto(BASE_URL)
    expect(page.locator("footer")).to_contain_text("Akanksha Yadav")


# ============================================================
# EDGE CASES & NEGATIVE TESTS
# ============================================================

def test_all_external_links_have_target_blank(page: Page):
    """All external links should open in a new tab (target=_blank)."""
    page.goto(BASE_URL)
    external_links = page.locator("a[href^='https']").all()
    for link in external_links:
        href = link.get_attribute("href")
        target = link.get_attribute("target")
        # Skip internal GitHub Pages links
        if "akanksha-avy.github.io" in (href or ""):
            continue
        assert target == "_blank", f"External link '{href}' missing target='_blank'"


def test_no_empty_href_links(page: Page):
    """No anchor tag should have an empty or '#' only href (broken links)."""
    page.goto(BASE_URL)
    links = page.locator("a").all()
    broken = []
    for link in links:
        href = link.get_attribute("href") or ""
        if href == "" or href == "#":
            text = link.inner_text().strip()
            broken.append(f"'{text}' has href='{href}'")
    assert broken == [], f"Found links with empty/hash-only href: {broken}"


def test_no_broken_images(page: Page):
    """All images should load without errors (naturalWidth > 0)."""
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    images = page.locator("img").all()
    for img in images:
        natural_width = img.evaluate("el => el.naturalWidth")
        src = img.get_attribute("src") or "unknown"
        assert natural_width > 0, f"Broken image: {src}"


def test_skill_cards_all_have_icons(page: Page):
    """Every skill card should have an emoji icon."""
    page.goto(BASE_URL)
    icons = page.locator(".skill-icon").all()
    for icon in icons:
        text = icon.inner_text().strip()
        assert text != "", "Skill card icon should not be empty"


def test_contact_section_has_three_buttons(page: Page):
    """Contact section should have exactly 3 action buttons (Email, LinkedIn, GitHub)."""
    page.goto(BASE_URL)
    expect(page.locator(".contact-links a")).to_have_count(3)


def test_hero_sub_text_mentions_dubai(page: Page):
    """Hero subtitle should mention Dubai as location."""
    page.goto(BASE_URL)
    expect(page.locator(".hero-sub")).to_contain_text("Dubai")


def test_hero_sub_text_mentions_available(page: Page):
    """Hero subtitle should mention availability."""
    page.goto(BASE_URL)
    sub_text = page.locator(".hero-sub").inner_text()
    assert "available" in sub_text.lower(), f"'available' not found in hero subtitle: {sub_text}"


def test_page_load_time(page: Page):
    """Page should load within 5 seconds — performance baseline."""
    import time
    start = time.time()
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    duration = time.time() - start
    assert duration < 5, f"Page took {duration:.2f}s to load — exceeds 5s threshold"