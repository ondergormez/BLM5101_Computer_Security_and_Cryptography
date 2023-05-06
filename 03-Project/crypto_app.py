import gradio
import rsa_gs


def generate_key_pair(key_size, public_exponent):

    # User input validation part
    if key_size == "":
        key_size = 8

    try:
        key_size = float(key_size)
    except ValueError:
        raise gradio.Error("Key size must be integer type")

    if (key_size != int(key_size)):
        raise gradio.Error("Key size must be integer type")

    if (key_size < 8 or key_size > 12):
        raise gradio.Error("Key size must be between 8 and 12")

    if public_exponent == "":
        public_exponent = 65537

    try:
        public_exponent = float(public_exponent)
    except ValueError:
        raise gradio.Error("Public exponent must be integer type")

    if (public_exponent != int(public_exponent)):
        raise gradio.Error("Public exponent must be integer type")

    if (rsa_gs.RSA_GS.is_prime(public_exponent) == False):
        raise gradio.Error("Public exponent must be prime number")

    if (public_exponent < 65537):
        raise gradio.Error("Public exponent must be graeter than 65537")

    public_key, private_key = rsa_gs.RSA_GS.generate_key_pair(
        int(key_size), int(public_exponent))

    public_exponent, modulus = public_key
    private_exponent, modulus = private_key

    return public_exponent, modulus, private_exponent


def encrypt_text(public_exponent, modulus, shift, plaintext):

    if public_exponent == "":
        public_exponent = 65537

    try:
        public_exponent = float(public_exponent)
    except ValueError:
        raise gradio.Error("Public exponent must be integer type")

    if (public_exponent != int(public_exponent)):
        raise gradio.Error("Public exponent must be integer type")

    if (rsa_gs.RSA_GS.is_prime(public_exponent) == False):
        raise gradio.Error("Public exponent must be prime number")

    if (public_exponent < 65537):
        raise gradio.Error("Public exponent must be graeter than 65537")

    try:
        modulus = float(modulus)
    except ValueError:
        raise gradio.Error("Modulus must be integer type")

    if (modulus != int(modulus)):
        raise gradio.Error("Modulus must be integer type")

    try:
        shift = float(shift)
    except ValueError:
        raise gradio.Error("Shift count must be integer type")

    if (shift != int(shift)):
        raise gradio.Error("Shift count must be integer type")

    return rsa_gs.RSA_GS.encrypt((int(public_exponent), int(modulus)),
                                 int(shift), plaintext)


def decrypt_text(private_exponent, modulus, ciphertext, shift):
    # TODO: Validate input parameters
    # TODO: Return Plaintext hex string like E2A8B7E49E9CE4B6AFE18C82E28B85E9A9B1E28B85

    try:
        private_exponent = float(private_exponent)
    except ValueError:
        raise gradio.Error("Private exponent must be integer type")

    if (private_exponent != int(private_exponent)):
        raise gradio.Error("Private exponent must be integer type")

    try:
        modulus = float(modulus)
    except ValueError:
        raise gradio.Error("Modulus must be integer type")

    if (modulus != int(modulus)):
        raise gradio.Error("Modulus must be integer type")

    try:
        shift = float(shift)
    except ValueError:
        raise gradio.Error("Shift count must be integer type")

    if (shift != int(shift)):
        raise gradio.Error("Shift count must be integer type")

    return rsa_gs.RSA_GS.decrypt((int(private_exponent), int(modulus)),
                                 ciphertext, int(shift))

# GUI (Graphical User Interface) part
post_processed_text_textbox = gradio.Textbox(
    label="Post Processed Text",
    placeholder="The result will be here after submission...")

post_processed_performance_textbox = gradio.Textbox(
    label="Post Processed Performance",
    placeholder="The result will be here after submission...")

with gradio.Blocks() as demo:
    with gradio.Tab("RSA Key Pair Generation"):
        with gradio.Row():
            with gradio.Column():
                key_size_textbox = gradio.Textbox(
                    label="Key Size (bit length)",
                    placeholder="Enter the key size (in bits)...\nDefault: 8")
                public_exponent_textbox_for_generation_input = gradio.Textbox(
                    label="Public Exponent (e)",
                    placeholder=
                    "Enter the public exponent (e)...\nDefault: 65537")

            with gradio.Column():
                public_exponent_textbox_for_generation_output = gradio.Textbox(
                    label="Public Exponent (e)",
                    placeholder="The result will be here after generation...")
                modulus_textbox_for_generation = gradio.Textbox(
                    label="Modulus (n)",
                    placeholder="The result will be here after generation...")
                private_exponent_textbox_for_generation = gradio.Textbox(
                    label="Private Exponent (d)",
                    placeholder="The result will be here after generation...")

        generate_button = gradio.Button("Generate RSA Key Pair")

    with gradio.Tab("Encryption"):
        with gradio.Row():
            with gradio.Column():
                public_exponent_textbox_for_encryption = gradio.Textbox(
                    label="Public Exponent (e)",
                    placeholder=
                    "Enter the public exponent (e)...\nDefault: 65537")
                modulus_textbox_for_encryption = gradio.Textbox(
                    label="Modulus (n)",
                    placeholder="Enter the modulus (n)...")
                shift_textbox_for_encryption = gradio.Textbox(
                    label="Shift Key", placeholder="Enter the shift value...")
                # Plaintext: Text that is not computationally tagged, specially formatted, or written in code.
                plaintext_textbox_for_encryption = gradio.Textbox(
                    label="Plaintext (Unencrypted Text)",
                    placeholder="Enter the words to be encrypted...")

            with gradio.Column():
                plaintext_hex_string_textbox_for_encryption = gradio.Textbox(
                    label="Plaintext Hex String",
                    placeholder="The result will be here after encryption...")
                # Ciphertext: Encrypted text transformed from plaintext using an encryption algorithm.
                ciphertext_textbox_for_encryption = gradio.Textbox(
                    label="Ciphertext (Encrypted Text)",
                    placeholder="The result will be here after encryption...")
                ciphertext_hex_string_textbox_for_encryption = gradio.Textbox(
                    label="Ciphertext Hex String",
                    placeholder="The result will be here after encryption...")
                ciphertext_hex_string_textbox_for_caesar = gradio.Textbox(
                    label="Ciphertext Hex String After Caesar",
                    placeholder=
                    "The result will be here after Caesar encryption...")

        encrypt_button = gradio.Button("Encrypt")

    with gradio.Tab("Decryption"):
        with gradio.Row():
            with gradio.Column():
                private_exponent_textbox_for_decryption = gradio.Textbox(
                    label="Private Exponent (d)",
                    placeholder="Enter the private exponent (d)...")
                modulus_textbox_for_decryption = gradio.Textbox(
                    label="Modulus (n)",
                    placeholder="Enter the modulus (n)...")
                # Ciphertext: Encrypted text transformed from plaintext using an encryption algorithm.
                ciphertext_textbox_for_decryption = gradio.Textbox(
                    label="Ciphertext (Encrypted Text)",
                    placeholder="Enter the words to be decrypted...")
                shift_textbox_for_decryption = gradio.Textbox(
                    label="Shift Key", placeholder="Enter the shift value...")

            with gradio.Column():
                # Plaintext: Text that is not computationally tagged, specially formatted, or written in code.
                plaintext_textbox_for_decryption = gradio.Textbox(
                    label="Plaintext (Unencrypted Text)",
                    placeholder="The result will be here after decryption...")
                plaintext_hex_string_textbox_for_decryption = gradio.Textbox(
                    label="Plaintext Hex String",
                    placeholder="The result will be here after decryption...")

        decrypt_button = gradio.Button("Decrypt")

    generate_button.click(generate_key_pair,
                          inputs=[
                              key_size_textbox,
                              public_exponent_textbox_for_generation_input
                          ],
                          outputs=[
                              public_exponent_textbox_for_generation_output,
                              modulus_textbox_for_generation,
                              private_exponent_textbox_for_generation
                          ])

    encrypt_button.click(encrypt_text,
                         inputs=[
                             public_exponent_textbox_for_encryption,
                             modulus_textbox_for_encryption,
                             shift_textbox_for_encryption,
                             plaintext_textbox_for_encryption
                         ],
                         outputs=[
                             ciphertext_textbox_for_encryption,
                             ciphertext_hex_string_textbox_for_encryption,
                             plaintext_hex_string_textbox_for_encryption,
                             ciphertext_hex_string_textbox_for_caesar
                         ])

    decrypt_button.click(decrypt_text,
                         inputs=[
                             private_exponent_textbox_for_decryption,
                             modulus_textbox_for_decryption,
                             ciphertext_textbox_for_decryption,
                             shift_textbox_for_decryption
                         ],
                         outputs=[
                             plaintext_textbox_for_decryption,
                             plaintext_hex_string_textbox_for_decryption
                         ])

# TODO: Uncomment demo.launch(share=True)
# demo.launch(share=True)
# server_port=8080
demo.launch()
