---
doc_id: "mta-wiki:1908"
title: "Character Skins"
source_title: "Character Skins"
source_url: "https://wiki.multitheftauto.com/wiki/Character_Skins"
revision_id: 82818
language: "en"
categories: ["ID_Lists"]
generated_at: "2026-07-26T16:10:32.782954+00:00"
---

# Character Skins

Skins that may be used as [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) models.

- [All Skins Page](mta://reference/misc/all-skins-page.md) (not recommended for slow Internet connection)

- [Special Skins Page](mta://reference/misc/special-skins-page.md)

- [Gang Skins](mta://reference/misc/gang-skins.md)

- [Female Skins](mta://reference/misc/female-skins.md)

- [Male Skins](mta://reference/misc/male-skins.md)

**Sectioned Skin Pages**

- [Skins Page 1](mta://reference/misc/skins-page-1.md): 0-29

- [Skins Page 2](mta://reference/misc/skins-page-2.md): 30-52

- [Skins Page 3](mta://reference/misc/skins-page-3.md): 53-73, 75-76

- [Skins Page 4](mta://reference/misc/skins-page-4.md): 77-99

- [Skins Page 5](mta://reference/misc/skins-page-5.md): 100-122

- [Skins Page 6](mta://reference/misc/skins-page-6.md): 123-144

- [Skins Page 7](mta://reference/misc/skins-page-7.md): 145-148, 150-167

- [Skins Page 8](mta://reference/misc/skins-page-8.md): 168-189

- [Skins Page 9](mta://reference/misc/skins-page-9.md): 190-207, 209-212

- [Skins Page 10](mta://reference/misc/skins-page-10.md): 213-234

- [Skins Page 11](mta://reference/misc/skins-page-11.md): 235-257

- [Skins Page 12](mta://reference/misc/skins-page-12.md): 258-289

- [Skins Page 13](mta://reference/misc/skins-page-13.md): 290-312

**Skin tables**

```
-- a complete table
allSkins = getValidPedModels()
-- separate tables
maleSkins = {
	  0,   1,   2,   3,   4,   5,   7,   8,  14,  15,
	 16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
	 26,  27,  28,  29,  30,  32,  33,  34,  35,  36,
	 37,  42,  43,  44,  45,  46,  47,  48,  49,  50,
	 51,  52,  57,  58,  59,  60,  61,  62,  65,  66,
	 67,  68,  70,  71,  72,  73,  78,  79,  80,  81,
	 82,  83,  84,  94,  95,  96,  97,  98,  99, 100,
	101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
	111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
	121, 122, 123, 124, 125, 126, 127, 128, 132, 133,
	134, 135, 136, 137, 142, 143, 144, 146, 147, 153,
	154, 155, 156, 158, 159, 160, 161, 162, 163, 164,
	165, 166, 167, 168, 170, 171, 173, 174, 175, 176,
	177, 179, 180, 181, 182, 183, 184, 185, 186, 187,
	188, 189, 200, 202, 203, 204, 206, 209, 210, 212,
	213, 217, 220, 221, 222, 223, 227, 228, 229, 230,
	234, 235, 236, 239, 240, 241, 242, 247, 248, 249,
	250, 252, 253, 254, 255, 258, 259, 260, 261, 262,
	264, 265, 266, 267, 268, 269, 270, 272, 273,
	274, 275, 276, 277, 278, 279, 280, 281, 282, 283,
	284, 285, 286, 287, 288, 289, 290, 291, 292, 293,
	294, 295, 296, 297, 299, 300, 301, 302, 303, 305,
	306, 307, 308, 309, 310, 311, 312
}
femaleSkins = {
	  6,   9,  10,  11,  12,  13,  31,  38,  39,  40,
	 41,  53,  54,  55,  56,  63,  64,  69,  75,  76,
	 77,  85,  86,  87,  88,  89,  90,  91,  92,  93,
	129, 130, 131, 138, 139, 140, 141, 145, 148, 150,
	151, 152, 157, 169, 172, 178, 190, 191, 192, 193,
	194, 195, 196, 197, 198, 199, 201, 205, 207, 211,
	214, 215, 216, 218, 219, 224, 225, 226, 231, 232,
	233, 237, 238, 243, 244, 245, 246, 251, 256, 257,
	263, 298, 304
}
```

## Notes

- Last valid skin ID: 312

- Unused IDs:

- 74 149 208

## Related Functions

- [getElementModel](mta://scripting/shared/functions/getelementmodel.md)

- [setElementModel](mta://scripting/shared/functions/setelementmodel.md)

- [getValidPedModels](mta://scripting/shared/functions/getvalidpedmodels.md)

## See Also

- [ID Lists](mta://reference/misc/id--474ae526.md)

- [Web Skin Model Viewer](https://sa-skins.netlify.app/mta)
