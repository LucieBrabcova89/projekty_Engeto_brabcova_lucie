from playwright.sync_api import Page
from playwright.sync_api import expect


#V tomto případě test kontroluje, zda po najetí myší na obrázek se zobrazí text: Kamkoli, kdykoli!

def test_obrazek (page: Page):
    page.goto("https://naskapitan.cz/#")

    div = page.locator("#plavby > div > div.row.portfolio-container > div > a > img").nth(0)

    div.hover()

    h4 = page.locator("#plavby > div > div.row.portfolio-container > div > div > h4").nth(0)
    assert h4.inner_text() == "Kamkoliv, kdykoliv!"

#V tomto případě test kontroluje, že po vložení testovacího emailu a kliknutí na tlačítko Potvrdit bude název stránky (záložky): Error Submitting Form
from playwright.sync_api import Page
def test_email(page: Page):
    page.context.tracing.start(screenshots=True, sources=True, snapshots=True)
    page.goto("https://naskapitan.cz/#")

    # click on cookies
    btn = page.locator("#termsfeed-com---nb .cc-nb-okagree")
    btn.click()

    input = page.locator("#mlb2-4978205 > div > div > div.ml-form-embedBody.ml-form-embedBodyHorizontal.row-form > form > div.ml-form-formContent.horozintalForm > div > div.ml-input-horizontal > div > div > input")
    input.fill("test@example.com")
    btn = page.wait_for_selector('button:has-text("Potvrdit")', timeout=10000)
    btn.click()

    """page.wait_for_timeout(6000)
    print(page.title())"""
    expect(page).to_have_title("Error Submitting Form",timeout=10000)
    assert page.title() == "Error Submitting Form"

#V tomto případě test kontroluje, že po kliknutí na šipku v zeleném poli vpravo dole, bude uživatel vracen na začátek stránky
def test_vraceni_nahoru(page: Page):
    page.goto("https://naskapitan.cz/#")

    # click on cookies
    btn = page.locator("#termsfeed-com---nb .cc-nb-okagree")
    btn.click()

    page.mouse.wheel(0, 15000)

    page.locator("#footer > div.container.footer-bottom.clearfix").scroll_into_view_if_needed()
    page.locator(".back-to-top").click()

    div = page.locator("#hero > div > div > div.col-lg-6.pt-5.pt-lg-0.order-2.order-lg-1.d-flex.flex-column.justify-content-center > h1:nth-child(3)")

    page.wait_for_timeout(2000)
    is_visible = page.evaluate("""

        () => {

            const el = document.querySelector('#hero > div > div > div.col-lg-6.pt-5.pt-lg-0.order-2.order-lg-1.d-flex.flex-column.justify-content-center > h1:nth-child(3)');

            if (!el) return false;

            const rect = el.getBoundingClientRect();

            return (

                rect.top >= 0 &&

                rect.left >= 0 &&

                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&

                rect.right <= (window.innerWidth || document.documentElement.clientWidth)

            );

        }

    """)
    #expect(div).to_be_in_viewport()
    
    assert is_visible
    
    




  
