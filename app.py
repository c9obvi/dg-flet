import flet as ft

def calculate_price(original_price, using_card):
    # Employee discount
    employee_discount = 0.35
    discounted_price = original_price * (1 - employee_discount)

    # Taxes
    sales_tax = 0.1016
    city_tax = 0.04
    ca_excise_tax = 0.156
    total_tax = discounted_price * (sales_tax + city_tax + ca_excise_tax)
    
    # Final price
    total_price = discounted_price + total_tax

    # Optional card fee
    if using_card:
        total_price += 3.00

    return total_price

def main(page: ft.Page):
    # Set the title of your page
    page.title = "Dr. Green Thumb's Price Calculator"
    
    # Create a TextField for user to input the original price
    txt_original_price = ft.TextField(value="0", label="Enter original price")
    
    # Create a Switch for user to indicate card usage
    sw_use_card = ft.Switch(value=False)
    card_label = ft.Text(value="Use card?", color="white")
    
    # Create a Row to display the Switch and its label
    card_row = ft.Row([sw_use_card, card_label])

    # Create a Button to trigger price calculation
    def on_calculate_click(e):
        final_price = calculate_price(
            float(txt_original_price.value),
            sw_use_card.value
        )
        page.add(ft.Text(value=f"Final Price: ${final_price:.2f}"))

    btn_calculate = ft.FilledButton(text="Calculate", on_click=on_calculate_click)

    # Add UI elements to page
    page.add(
        ft.Column(
            [
                txt_original_price,
                card_row,
                btn_calculate
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
