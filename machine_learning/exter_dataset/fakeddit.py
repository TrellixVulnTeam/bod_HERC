import os
from machine_learning.exter_dataset.uitls.download import google_download_file, zip_download


url2 = "https://drive.google.com/file/d/1cjY6HsHaSZuLVHywIxD5xQqng33J5S2b"
url1 = "https://drive.google.com/drive/folders/150sL4SNi5zFK8nmllv5prWbn0LyvLzvo"

download_url = "https://doc-0s-58-docs.googleusercontent.com/docs/securesc/b9cr4k7tghjb5t6otaiu7579utvtc2af/tl7pe8na2r9f6pivjahn1vldr43iaibi/1659333600000/11360321380153708296/18190118699216058600/1hjcLrwMOGJBHrB6bqlaIhn6N09X0lr85?e=download&ax=AI9vYm5S2GJWJTseI0SQtA2YCj4zVBLhPqEIuGYHrnCQoZAcDYty6YkUbxVA-vmAa654-dEmgeJgMxeUYF83EBed59AursmieLbvlgqwiNgOz62b-fIvi4i4TPFxY23cgy8lwviCT_jmTan_eV2P8zhZhNP-CDYOcKLI-LZYqUWwulBAOcxxSxUVZXpi_SSA-qdKxuN8XbPXCp_4I8Eqg2fzScES_3tj83ksh16RYDHgIS8eQ2SG8zEQtqINedzaz-bq6AQhWAmxn4WPJQWCFWVH3Zzp9OOyd0ru8Us0JuwE2KJYBgh_yYU545rL2_j96CY-5PFLdJmG_Fn-RI0t9jB8Bu-TOXmY30lBblbF8Ro7v2efP0v-mw_CdceqYshIyIWf3qkq4Sh5YqRa22Xn1IlnP_ZY9MDkaf3Of2XEKQEXoftal0X7gA2KASEH9Pc9Ru9UnL1EwJKAp6CokUU9Qoo1Trt2uKAbaJITnPi6n_zaN8GMP2CKL3RROZzjPB8nsQAlJ44p1VCx0Q8_mUNDZlVolSMxFTI08YFueGXI9arLVZy5XK-32o_MFAjJJ6mZT_pCTcTFfCC1XaBoXXMGVPZpDYmbpc7Q1dwIthmw0oro7s06uqfzrZQ-lOB4lqJa62Lzp8ys3TpLa1asiswSdJLdmJl4I0HTpzqycaMO9gn_OZwvrPi7ayGF1CYuEU3X7Jta6DYYZQIj81hvsA&uuid=8e5e71a3-2185-45ce-88e6-a04d81d031e6&authuser=0&nonce=ar6mhtg730dog&user=18190118699216058600&hash=l2kb3dgom742g5cqek9li7qpk8ohrff7"



base_path = os.path.dirname(os.path.realpath(__file__))
google_download_file(base_path,"fakeddit","1cjY6HsHaSZuLVHywIxD5xQqng33J5S2b","public_images.tar.bz2")


def get_data():
    pass