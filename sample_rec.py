# modules
from PIL import Image


# this should be modified !
# the .jpg file should be exactly 120 x 200 !
img_name = 'leimu_rec' # should be the same as the image name without the extension

# zipping fact
g_cutfact = 4

Note = open('main.c', mode='w')

# the main functions
Note.write(
    """
#include "stm32f10x.h"
#include "EIE3810_TFTLCD.h"


void Delay(u32);
void EIE3810_Pure_Drawing();

void Delay(u32 count) // Use looping for delay
{
	u32 i;
	for (i = 0; i < count; i++)
		;
}

int main(void)
{
	EIE3810_TFTLCD_Init();
	Delay(1000000);

    EIE3810_Pure_Drawing();
}

void EIE3810_Pure_Drawing()
{
"""
)


img = Image.open('{0}.jpg'.format(img_name))
width, height = img.size


for y in range(0, height):
    for x in range(0, width):
        pixel = img.getpixel((x, y))
        r, g, b = pixel
        r = (r >> 3) & 0x1F  # 0x1F = 00011111
        g = (g >> 2) & 0x3F  # 0x3F = 00111111
        b = (b >> 3) & 0x1F  # 0x1F = 00011111
        rgb565 = (b << 0) + (g << 5) + (r << 11)
        Note.write("    EIE3810_TFTLCD_FillRectangle({0}, {1}, {2}, {3}, {4});\n"
                   .format(x*g_cutfact, g_cutfact, y*g_cutfact, g_cutfact, hex(rgb565)))


Note.write(
    """
} 
"""
)

Note.close()
