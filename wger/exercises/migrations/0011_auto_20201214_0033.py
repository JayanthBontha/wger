# Generated by Django 3.1.4 on 2020-12-13 23:33

from django.db import migrations

exercise_mapping = [
    # 111	c4856da3-8454-4857-8997-336d06df590f	Squats
    #  7	36c27886-b10b-41b6-ac60-f02ee3784041	Kniebeuge
    # 608	993cf4e0-e664-4cc2-aa46-683c6fc7a74f	Приседания
    {'en': 'c4856da3-8454-4857-8997-336d06df590f',
     'de': '36c27886-b10b-41b6-ac60-f02ee3784041',
     'ru': '993cf4e0-e664-4cc2-aa46-683c6fc7a74f'},

    # 160	b1d6d536-7f4a-4dd3-8b76-62d7a984e115	Pistol Squat
    # 358	40a0019e-eaf2-491f-a134-9fdd51121358	Einbeinige Kniebeuge (Pistol Squat)
    {'en': 'b1d6d536-7f4a-4dd3-8b76-62d7a984e115', 'de': '40a0019e-eaf2-491f-a134-9fdd51121358'},

    # 346	1d90f3a8-56e4-4c15-a4b4-94fc0e114e8c	Bulgarian Split Squat
    # 695	cf21383b-b96a-40b5-b047-b9c3ddcab963	Bulgarian Split Squat
    {'en': '1d90f3a8-56e4-4c15-a4b4-94fc0e114e8c', 'de': 'cf21383b-b96a-40b5-b047-b9c3ddcab963'},

    # 202	eed05679-d1cb-44a2-a17d-dd5b0097c874	Pendelay Rows
    # 731	196f9a72-7518-45c4-a4f2-d3ba3e0d3b3e	Pendelay Rows
    {'en': 'eed05679-d1cb-44a2-a17d-dd5b0097c874', 'de': '196f9a72-7518-45c4-a4f2-d3ba3e0d3b3e'},

    # 130	2966e4a2-4306-4cb5-a2dc-8951cd192555	Leg Press on Hackenschmidt Machine
    # 402	634dcf89-c346-4af8-8b09-61f238798877	Kniebeuge an Hackenschmidtmaschine
    {'en': '2966e4a2-4306-4cb5-a2dc-8951cd192555', 'de': '634dcf89-c346-4af8-8b09-61f238798877'},

    # 104	e7677699-5e4f-49e6-a645-e8915a203c4d	Calf Raises on Hackenschmitt Machine
    # 23	c7b98fb5-7723-471a-92a1-7b4e892a5468	Wadenheben an Hackenschmidt
    {'en': 'e7677699-5e4f-49e6-a645-e8915a203c4d', 'de': 'c7b98fb5-7723-471a-92a1-7b4e892a5468'},

    # 105	22cca8fc-cfaf-4941-b0f7-faf9f2937c52	Deadlifts
    #  9	521a5e4f-6f35-43e5-9d1c-6e75c4956e96	Kreuzheben
    {'en': '22cca8fc-cfaf-4941-b0f7-faf9f2937c52', 'de': '521a5e4f-6f35-43e5-9d1c-6e75c4956e96'},

    # 570	f4dd363c-b49c-419a-b8ae-0d8e18728d8e	Sumo Squats
    # 762	b399006c-bb45-451e-908e-1b279b2a42a6	Sumo Squats (Pilé Squats) Kniebeuge
    {'en': 'f4dd363c-b49c-419a-b8ae-0d8e18728d8e', 'de': 'b399006c-bb45-451e-908e-1b279b2a42a6'},

    # 91	d325dd5c-6833-41c7-8eea-6b95c4871133	Crunches
    #  4	0e10ac9b-ed1d-42c9-b8cc-123c22ccc5d5	Crunches
    {'en': 'd325dd5c-6833-41c7-8eea-6b95c4871133', 'de': '0e10ac9b-ed1d-42c9-b8cc-123c22ccc5d5'},

    # 92	8d6c13c6-256d-4137-b1c6-b0e817697639	Crunches With Cable
    # 33	5c47b690-d19f-4523-9c47-47160693eefc	Crunches am Seil
    {'en': '8d6c13c6-256d-4137-b1c6-b0e817697639', 'de': '5c47b690-d19f-4523-9c47-47160693eefc'},

    # 94	6709577b-95ec-4053-a822-d5fe1f753966	Crunches on Machine
    # 51	efbece79-4384-49d1-bb88-e16fcd8de5aa	Crunches an Maschine
    {'en': '6709577b-95ec-4053-a822-d5fe1f753966', 'de': 'efbece79-4384-49d1-bb88-e16fcd8de5aa'},

    # 307	1b8b1657-40fd-4e3b-97b7-1c79b1079f8e	Bear Walk
    # 718	e4b3da5b-1803-42af-a50e-ffbac3853cd0	Bear Walk
    {'en': '1b8b1657-40fd-4e3b-97b7-1c79b1079f8e', 'de': 'e4b3da5b-1803-42af-a50e-ffbac3853cd0'},

    # 192	5da6340b-22ec-4c1b-a443-eef2f59f92f0	Bench Press
    # 15	198dcb2e-e35f-4b69-ae8b-e1124d438eae	Bankdrücken LH
    {'en': '5da6340b-22ec-4c1b-a443-eef2f59f92f0', 'de': '198dcb2e-e35f-4b69-ae8b-e1124d438eae'},

    # 88	03d821e7-e1ac-4026-903b-d406381cbf76	Bench Press Narrow Grip
    # 38	4def60e7-ed8d-4a9d-bf76-ceb15ecf9779	Bankdrücken Eng
    {'en': '03d821e7-e1ac-4026-903b-d406381cbf76', 'de': '4def60e7-ed8d-4a9d-bf76-ceb15ecf9779'},

    # 97	0ec76f5d-1311-4d6d-bf79-00fa17c3061a	Benchpress Dumbbells
    # 77	06450bcb-03a8-4bd7-8349-ef677ee57ea3	Bankdrücken KH
    {'en': '0ec76f5d-1311-4d6d-bf79-00fa17c3061a', 'de': '06450bcb-03a8-4bd7-8349-ef677ee57ea3'},

    # 129	8c6c1544-cbf8-403c-ae12-b27b392702f8	Biceps Curl With Cable
    # 3	ef487de3-f071-41bf-85a6-6e76afe9c732	Bizeps am Kabel
    {'en': '8c6c1544-cbf8-403c-ae12-b27b392702f8', 'de': 'ef487de3-f071-41bf-85a6-6e76afe9c732'},

    # 80	38919515-ce04-4383-9c3f-5846edd0e844	Biceps Curls With SZ-bar
    # 44	8277124a-9ef2-442a-9824-7ab4439a5f1f	Bizeps Curls Mit ß-Stange
    {'en': '38919515-ce04-4383-9c3f-5846edd0e844', 'de': '8277124a-9ef2-442a-9824-7ab4439a5f1f'},

    # 74	c56078d2-ae85-4524-a467-d1e143b6df1a	Biceps Curls With Barbell
    # 24	2e3fa138-3894-4f61-959a-d8966804a1a3	Bizeps LH-Curls
    {'en': 'c56078d2-ae85-4524-a467-d1e143b6df1a', 'de': '2e3fa138-3894-4f61-959a-d8966804a1a3'},

    # 275	dfa090e4-77ae-40ed-86c0-4696fe93dcf1	Dumbbell Concentration Curl
    # 681	ec0c53a5-15b9-4c2f-ac7c-00888db9f8ee	Konzentrations-Curls
    {'en': 'dfa090e4-77ae-40ed-86c0-4696fe93dcf1', 'de': 'ec0c53a5-15b9-4c2f-ac7c-00888db9f8ee'},

    # 86	6dcc9adb-939c-4581-9e44-d0d73753997b	Hammercurls
    # 46	ff454f5a-70ee-40fb-9200-5e7e42960ef0	Hammercurls
    {'en': '6dcc9adb-939c-4581-9e44-d0d73753997b', 'de': 'ff454f5a-70ee-40fb-9200-5e7e42960ef0'},

    # 138	5baf40e5-ea3c-4f8d-b60a-d294ee2de55b	Hammercurls on Cable
    # 134	06e9de49-ac1b-45c1-b289-475118932434	Hammercurls am Seil
    {'en': '5baf40e5-ea3c-4f8d-b60a-d294ee2de55b', 'de': '06e9de49-ac1b-45c1-b289-475118932434'},

    # 771	bdcae845-6726-457f-8e04-203754a78e1c	Reverse Curl
    # 815	7662a76a-3ea7-4b63-86d9-c0702b554090	Reverse Curls
    {'en': 'bdcae845-6726-457f-8e04-203754a78e1c', 'de': '7662a76a-3ea7-4b63-86d9-c0702b554090'},

    # 298	fa56d30a-7a8f-4084-aa68-46bd52f97959	Dumbbell Incline Curl
    # 242	0842e81e-7b90-4d68-8e6b-e9a7c0186b54	Bizeps KH-Curls Schrägbank
    {'en': 'fa56d30a-7a8f-4084-aa68-46bd52f97959', 'de': '0842e81e-7b90-4d68-8e6b-e9a7c0186b54'},

    # 81	48a59aa8-4568-409c-8afe-f8cb99c558ea	Biceps Curls With Dumbbell
    # 26	8cbbffcc-1989-43de-9200-03869480398c	Bizeps KH-Curls
    {'en': '48a59aa8-4568-409c-8afe-f8cb99c558ea', 'de': '8cbbffcc-1989-43de-9200-03869480398c'},

    # 227	53ca25b3-61d9-4f72-bfdb-492b83484ff5	Arnold Shoulder Press
    # 228	880bff63-6798-4ffc-a818-b2a1ccfec0f7	Arnold Press
    {'en': '53ca25b3-61d9-4f72-bfdb-492b83484ff5', 'de': '880bff63-6798-4ffc-a818-b2a1ccfec0f7'},

    # 150	3721be0c-2a59-4bb9-90d3-695faaf028af	Shrugs, Barbells
    # 137	a63d40df-a872-44e7-87d2-9b58b67d5406	Shrugs (Schulterheben) Mit LH
    {'en': '3721be0c-2a59-4bb9-90d3-695faaf028af', 'de': 'a63d40df-a872-44e7-87d2-9b58b67d5406'},

    # 151	ee61aef0-f0c7-4a7a-882a-3b39312dfffd	Shrugs, Dumbbells
    # 8	6dde45fc-7fdf-4523-a039-9c373677a750	Shrugs (Schulterheben) Mit KH
    {'en': 'ee61aef0-f0c7-4a7a-882a-3b39312dfffd', 'de': '6dde45fc-7fdf-4523-a039-9c373677a750'},

    # 387	b229c57f-5363-41e2-add7-c2501a31de0b	Wall Squat
    # 707	7f3e45fa-3b17-4cdb-90d5-cb9957212cbf	Wall Squat
    {'en': 'b229c57f-5363-41e2-add7-c2501a31de0b', 'de': '7f3e45fa-3b17-4cdb-90d5-cb9957212cbf'},

    # 93	4bd55b0a-559a-4458-aabd-e66619b63610	Negative Crunches
    # 32	f5e98b51-6c0e-4c77-94ec-158210669f6d	Crunches an Negativbank
    {'en': '4bd55b0a-559a-4458-aabd-e66619b63610', 'de': 'f5e98b51-6c0e-4c77-94ec-158210669f6d'},

    # 330	6572a8e9-083c-4622-8f0c-6107a013a490	Superman
    # 735	bd58585e-4bf4-46cc-ba38-717a7857e21c	Superman
    {'en': '6572a8e9-083c-4622-8f0c-6107a013a490', 'de': 'bd58585e-4bf4-46cc-ba38-717a7857e21c'},

    # 238	7729ffe5-a896-4deb-80e0-f4e6163c0c09	Plank
    # 417	257cdb33-ba8b-410a-9396-5132b08dc912	Unterarmstütze - Plank
    {'en': '7729ffe5-a896-4deb-80e0-f4e6163c0c09', 'de': '257cdb33-ba8b-410a-9396-5132b08dc912'},

    # 325	a36f852f-a29f-4f93-81b6-1012047ac1ee	Side Plank
    # 715	2c6cd166-40e1-4b68-96b7-c30b31e28b99	Side Plank
    {'en': 'a36f852f-a29f-4f93-81b6-1012047ac1ee', 'de': '2c6cd166-40e1-4b68-96b7-c30b31e28b99'},

    # 116	6e862700-3d63-486c-99ae-744c68d2f753	Good Mornings
    # 50	a311a463-f219-4741-b4fb-247013dc8dd8	Good Mornings
    {'en': '6e862700-3d63-486c-99ae-744c68d2f753', 'de': 'a311a463-f219-4741-b4fb-247013dc8dd8'},

    # 326	bf9e572d-d138-43e9-a486-a5c6ad9033f8	Full Sit Outs
    # 710	143cf744-ce94-458c-9c74-1aea6c64cfc7	Full Sit Outs
    {'en': 'bf9e572d-d138-43e9-a486-a5c6ad9033f8', 'de': '143cf744-ce94-458c-9c74-1aea6c64cfc7'},

    # 95	fb750082-7034-4c51-b1e4-dfa0fe2dac8e	Sit-ups
    # 57	60f329dd-f8ab-469a-8a88-39f80275b3a7	Sit Ups
    {'en': 'fb750082-7034-4c51-b1e4-dfa0fe2dac8e', 'de': '60f329dd-f8ab-469a-8a88-39f80275b3a7'},

    # 83	aa4fcd9b-baee-41cf-b4c5-8462bc43a8be	Dips Between Two Benches
    # 68	011b956d-33b3-4600-9e42-2e7dcbac9fb5	Dips Zwischen 2 Bänke
    {'en': 'aa4fcd9b-baee-41cf-b4c5-8462bc43a8be', 'de': '011b956d-33b3-4600-9e42-2e7dcbac9fb5'},

    # 354	6335de72-146f-4f38-886d-6b8a27db62ff	Burpees
    # 719	5bae16b0-cefb-4fc7-be2b-e31794335c42	Burpees
    {'en': '6335de72-146f-4f38-886d-6b8a27db62ff', 'de': '5bae16b0-cefb-4fc7-be2b-e31794335c42'},

    # 289	6add5973-86d0-4543-928a-6bb8b3f34efc	Axe Hold
    # 677	8e9d8968-323d-468c-9174-8cf11a105fad	Axe Hold
    {'en': '6add5973-86d0-4543-928a-6bb8b3f34efc', 'de': '8e9d8968-323d-468c-9174-8cf11a105fad'},

    # 98	3c3857f8-d224-4d5a-8cc1-f4e7982d3475	Butterfly
    # 30	9df24c6f-016b-4623-8878-f71c235c50fa	Butterfly
    {'en': '3c3857f8-d224-4d5a-8cc1-f4e7982d3475', 'de': '9df24c6f-016b-4623-8878-f71c235c50fa'},

    # 99	08637e04-d995-4c07-b021-a20f26b6fd97	Butterfly Narrow Grip
    # 52	44b0d79a-5c5b-43df-bf62-3e67148f1c33	Butterfly Eng
    {'en': '08637e04-d995-4c07-b021-a20f26b6fd97', 'de': '44b0d79a-5c5b-43df-bf62-3e67148f1c33'},

    # 124	8715a96e-c8a2-458a-b023-4ea7d82fdab8	Butterfly Reverse
    # 21	605b4a25-bc1d-4604-bd93-c85b2aaf84ae	Butterfly Reverse
    {'en': '8715a96e-c8a2-458a-b023-4ea7d82fdab8', 'de': '605b4a25-bc1d-4604-bd93-c85b2aaf84ae'},

    # 394	659f3fb9-2370-42fb-9c29-9aaf65c7a7de	Facepull
    # 415	237c8770-4c1f-433d-b8b4-b1ae5c69bbc5	Face Pulls
    {'en': '659f3fb9-2370-42fb-9c29-9aaf65c7a7de', 'de': '237c8770-4c1f-433d-b8b4-b1ae5c69bbc5'},

    # 281	e1881607-9418-4bcc-8c69-2301a579637e	L Hold
    # 753	6ae461d7-daea-4ac7-999b-826fe28263b0	L Hold
    {'en': 'e1881607-9418-4bcc-8c69-2301a579637e', 'de': '6ae461d7-daea-4ac7-999b-826fe28263b0'},

    # 143	b192c4eb-31c6-458e-b566-d3f38b5aa30c	Long-Pulley (low Row)
    # 37	91fa0487-b137-4bef-86cf-39816cd5ee48	Long-Pulley
    {'en': 'b192c4eb-31c6-458e-b566-d3f38b5aa30c', 'de': '91fa0487-b137-4bef-86cf-39816cd5ee48'},

    # 144	bcabc8cf-c005-4630-8853-ef4922e7fd91	Long-Pulley, Narrow
    # 136	490a615c-4185-4560-88a5-020f3aa40be2	Long-Pulley (eng)
    {'en': 'bcabc8cf-c005-4630-8853-ef4922e7fd91', 'de': '490a615c-4185-4560-88a5-020f3aa40be2'},

    # 103	399666e7-30a7-4b86-833d-4422e4c72b61	Sitting Calf Raises
    # 14	47b4d57a-3bb3-4a03-a522-a0559a254730	Wadenheben Sitzend
    {'en': '399666e7-30a7-4b86-833d-4422e4c72b61', 'de': '47b4d57a-3bb3-4a03-a522-a0559a254730'},

    # 102	abc4c62e-27b2-4c31-8766-40f8dca84cab	Standing Calf Raises
    # 13	283d4ec5-1b29-41bb-997d-74c30e7a68b5	Wadenheben Stehend
    {'en': 'abc4c62e-27b2-4c31-8766-40f8dca84cab', 'de': '283d4ec5-1b29-41bb-997d-74c30e7a68b5'},

    # 308	074530d6-801a-404b-b3b7-adc207be69be	Calf Press Using Leg Press Machine
    # 745	84afd45e-235a-41c3-8711-ea9f6d08eeb6	Wadendrücken an Beinpresse
    {'en': '074530d6-801a-404b-b3b7-adc207be69be', 'de': '84afd45e-235a-41c3-8711-ea9f6d08eeb6'},

    # 85	ee00d53e-4482-44aa-b780-bbc570061841	French Press (skullcrusher) Dumbbells
    # 58	bdf8997a-84ce-434a-ae95-1f9fc50f43bb	Frenchpress KH
    {'en': 'ee00d53e-4482-44aa-b780-bbc570061841', 'de': 'bdf8997a-84ce-434a-ae95-1f9fc50f43bb'},

    # 84	ee4a350b-c681-407f-a414-6ec243809ec7	French Press (skullcrusher) SZ-bar
    # 25	9972e42d-43d8-43c0-b547-4638ca3e47be	Frenchpress ß-Stange
    {'en': 'ee4a350b-c681-407f-a414-6ec243809ec7', 'de': '9972e42d-43d8-43c0-b547-4638ca3e47be'},

    # 788	6c8e863c-f6c2-4ad0-a0e9-5e6d9e6a928b	Leg Press
    # 6	a27cfdd9-5299-49ab-85f5-6e4042657549	Beinpresse
    {'en': '6c8e863c-f6c2-4ad0-a0e9-5e6d9e6a928b', 'de': 'a27cfdd9-5299-49ab-85f5-6e4042657549'},

    # 115	560e1a20-33e1-45db-ba5b-63f8c51af76d	Leg Presses (narrow)
    # 54	e7d0cc2d-e28b-479f-91d9-7eab7b686fd8	Beinpresse Eng
    {'en': '560e1a20-33e1-45db-ba5b-63f8c51af76d', 'de': 'e7d0cc2d-e28b-479f-91d9-7eab7b686fd8'},

    # 112	587c0052-f2bc-48ca-8af9-415175308901	Dumbbell Lunges Standing
    # 55	27301836-ed7f-4510-83e7-66c0b8041a44	Ausfallschritte Stehend
    # 363	c38e34a7-5560-46a1-bae4-c4fce9619e55	Výpad Statický
    {'en': '587c0052-f2bc-48ca-8af9-415175308901',
     'de': '27301836-ed7f-4510-83e7-66c0b8041a44',
     'cs': 'c38e34a7-5560-46a1-bae4-c4fce9619e55'},

    # 113	ffd4ce7e-e14f-49d4-9dc9-dc1362631382	Dumbbell Lunges Walking
    # 5	5675ae61-6597-4806-ae5c-2dda5a5ac03c	Ausfallschritte im Gehen
    {'en': 'ffd4ce7e-e14f-49d4-9dc9-dc1362631382', 'de': '5675ae61-6597-4806-ae5c-2dda5a5ac03c'},

    # 145	754391c6-39d5-4bb6-a311-68a520f6fd3a	Fly With Dumbbells
    # 18	c0119734-a412-4f34-91f1-cd1c1177fcb8	Fliegende KH Flachbank
    {'en': '754391c6-39d5-4bb6-a311-68a520f6fd3a', 'de': 'c0119734-a412-4f34-91f1-cd1c1177fcb8'},

    # 146	acf1f2df-46c4-49a3-8e6c-2979ea4204b1	Fly With Dumbbells, Decline Bench
    # 73	3b34d81d-7882-46a6-bb83-40f84d3f8300	Fliegende KH Schrägbank
    {'en': 'acf1f2df-46c4-49a3-8e6c-2979ea4204b1', 'de': '3b34d81d-7882-46a6-bb83-40f84d3f8300'},

    # 409	75ec610d-216a-49fe-b395-c5fd8ee14b53	Reverse Plank
    # 713	24e5637e-60eb-41f5-b964-31e2af990bfc	Reverse Plank
    {'en': '75ec610d-216a-49fe-b395-c5fd8ee14b53', 'de': '24e5637e-60eb-41f5-b964-31e2af990bfc'},

    # 181	f6c4e2fa-226d-46e8-87dc-75fc8cd628bd	Chin-ups
    # 747	9e71d2a3-9021-4270-a7b9-0d8bd28e7394	Chin-ups
    {'en': 'f6c4e2fa-226d-46e8-87dc-75fc8cd628bd', 'de': '9e71d2a3-9021-4270-a7b9-0d8bd28e7394'},

    # 346	1d90f3a8-56e4-4c15-a4b4-94fc0e114e8c	Bulgarian Split Squat
    # 695	cf21383b-b96a-40b5-b047-b9c3ddcab963	Bulgarian Split Squat
    {'en': '1d90f3a8-56e4-4c15-a4b4-94fc0e114e8c', 'de': 'cf21383b-b96a-40b5-b047-b9c3ddcab963'},

    # 781	7191e015-0c60-4376-9be0-733b9754b7f8	Dips
    # 29	41b495fd-562e-4d6e-942a-60dc52d5e194	Dips
    {'en': '7191e015-0c60-4376-9be0-733b9754b7f8', 'de': '41b495fd-562e-4d6e-942a-60dc52d5e194'},

    # 279	88568115-5e88-4afc-b005-e2f7d453ac13	Tricep Dumbbell Kickback
    # 232	ebe60386-bf33-4f50-87a6-d44c5f454158	Kick-Backs
    {'en': '88568115-5e88-4afc-b005-e2f7d453ac13', 'de': 'ebe60386-bf33-4f50-87a6-d44c5f454158'},

    # 128	f57a0c60-7d37-4eb3-a94e-1a90292e8c02	Hyperextensions
    # 60	913d71cc-ba7a-4902-bfa8-3c5203129d72	Hyperextensions
    {'en': 'f57a0c60-7d37-4eb3-a94e-1a90292e8c02', 'de': '913d71cc-ba7a-4902-bfa8-3c5203129d72'},

    # 195	9d756e84-6b77-4f17-b21d-7d266d6a8bd2	Push Ups
    # 172	35871103-6cfe-493f-afe1-8401f88fed84	Liegestütz
    {'en': '9d756e84-6b77-4f17-b21d-7d266d6a8bd2', 'de': '35871103-6cfe-493f-afe1-8401f88fed84'},

    # 260	36ef5f12-6f77-4754-a926-39915e4b57a5	Decline Pushups
    # 721	e386cd27-aef6-4565-88ad-639b0ea04e3a	Negativ Pushups
    {'en': '36ef5f12-6f77-4754-a926-39915e4b57a5', 'de': 'e386cd27-aef6-4565-88ad-639b0ea04e3a'},

    # 139	88bbdbde-c9b6-45a1-aee9-efc6f02cfab3	Triceps Machine
    # 27	ca03dd79-4a92-47ef-a461-e67ccc406f82	Trizepsmaschine
    {'en': '88bbdbde-c9b6-45a1-aee9-efc6f02cfab3', 'de': 'ca03dd79-4a92-47ef-a461-e67ccc406f82'},

    # 338	20b88059-3958-4184-9134-b48656ad868d	Isometric Wipers
    # 724	666d1c77-d74b-411c-be3e-1e60a02c548d	Isometric Wipers
    {'en': '20b88059-3958-4184-9134-b48656ad868d', 'de': '666d1c77-d74b-411c-be3e-1e60a02c548d'},

    # 90	20a76bd0-1e56-4a4e-bd79-0ab118552bde	Triceps Extensions on Cable With Bar
    # 63	60aab5bf-ff7a-4e50-9e92-1f4813c3da75	Trizeps Seildrücken Mit Stange
    {'en': '20a76bd0-1e56-4a4e-bd79-0ab118552bde', 'de': '60aab5bf-ff7a-4e50-9e92-1f4813c3da75'},

    # 89	f1b5e525-6232-4d60-a243-9b2cd6c55298	Triceps Extensions on Cable
    #  1	b83e3d85-a53d-4939-a61c-7baa2e94d358	Trizeps Seildrücken
    {'en': 'f1b5e525-6232-4d60-a243-9b2cd6c55298', 'de': 'b83e3d85-a53d-4939-a61c-7baa2e94d358'},

    # 270	625aefd5-7ba2-40e9-bdc3-7d3ab1bcf3b8	Pause Bench
    # 725	5009eedc-554f-43ef-852e-77ba45a7297c	Pause Bench
    {'en': '625aefd5-7ba2-40e9-bdc3-7d3ab1bcf3b8', 'de': '5009eedc-554f-43ef-852e-77ba45a7297c'},

    # 149	79a3a34c-262f-4cae-b827-b5a85b11b860	Lateral Raises on Cable, One Armed
    # 132	382731d2-ae07-4a3c-a055-09dadd5f12e0	Seitheben am Kabel, Einarmig
    {'en': '79a3a34c-262f-4cae-b827-b5a85b11b860', 'de': '382731d2-ae07-4a3c-a055-09dadd5f12e0'},

    # 148	5345766a-c092-457a-aa21-8ee6ffa855d4	Lateral Raises
    # 20	72e78f4d-65f7-4ddd-9247-cdc1e133fa80	Seitheben KH
    {'en': '5345766a-c092-457a-aa21-8ee6ffa855d4', 'de': '72e78f4d-65f7-4ddd-9247-cdc1e133fa80'},

    # 191	f2e563d2-507b-4586-88c8-77652cd19648	Front Squats
    # 390	d23d1980-3a50-4d3f-8123-90d7e55c7804	Front Kniebeuge
    {'en': 'f2e563d2-507b-4586-88c8-77652cd19648', 'de': 'd23d1980-3a50-4d3f-8123-90d7e55c7804'},

    # 229	89e6d2ea-9a17-4a77-9a52-d5bcf39d57fd	Military Press
    # 153	47c33837-be38-4ebb-b19a-84c280f5f2b0	Frontdrücken LH
    {'en': '89e6d2ea-9a17-4a77-9a52-d5bcf39d57fd', 'de': '47c33837-be38-4ebb-b19a-84c280f5f2b0'},

    # 854	37097633-de80-4271-9b7c-291f359e0ef4	Hip Thrust
    # 230	981ef1f0-414a-478b-bc1b-9c6afa45bc77	Beckenheben
    {'en': '37097633-de80-4271-9b7c-291f359e0ef4', 'de': '981ef1f0-414a-478b-bc1b-9c6afa45bc77'},

    # 177	a24a0521-6391-419c-bd89-795bba0eb5ee	Leg Extension
    # 133	da7fccca-941e-457a-a2eb-d0c56d419938	Beinbeuger Sitzend
    {'en': 'a24a0521-6391-419c-bd89-795bba0eb5ee', 'de': 'da7fccca-941e-457a-a2eb-d0c56d419938'},

    # 109	f82c579e-c069-4dc7-8e36-a3266dfd8e4a	Bent Over Rowing
    # 59	126d719a-4b59-4458-b182-d578cdcfee1a	Rudern Vorgebeugt LH
    {'en': 'f82c579e-c069-4dc7-8e36-a3266dfd8e4a', 'de': '126d719a-4b59-4458-b182-d578cdcfee1a'},

    # 108	57747eb3-411a-4efd-8842-a45e562320ee	Rowing, Seated
    # 245	788ef0a5-492f-48a7-87dc-b15dda185bb8	Rudern Eng Zum Bauch
    {'en': '57747eb3-411a-4efd-8842-a45e562320ee', 'de': '788ef0a5-492f-48a7-87dc-b15dda185bb8'},

    # 119	9926e18f-4e2b-4c20-9477-9bfb08d229bc	Shoulder Press, Barbell
    # 266	197600e7-9bb2-448c-baca-244d679e7b07	Schulterdrücken LH
    {'en': '9926e18f-4e2b-4c20-9477-9bfb08d229bc', 'de': '197600e7-9bb2-448c-baca-244d679e7b07'},

    # 123	1df6a1b5-7bd2-402f-9d5e-94f9ed6d8b54	Shoulder Press, Dumbbells
    # 241	0d4390ea-51dc-42dc-94af-ba0e94a73484	Schulterdrücken KH
    {'en': '1df6a1b5-7bd2-402f-9d5e-94f9ed6d8b54', 'de': '0d4390ea-51dc-42dc-94af-ba0e94a73484'},

    # 107	7ce6b090-5099-4cd0-83ae-1a02725c868b	Pull-ups
    # 36	4e741c73-d40a-4fad-b0e0-76edd9bbe8df	Klimmzüge
    {'en': '7ce6b090-5099-4cd0-83ae-1a02725c868b', 'de': '4e741c73-d40a-4fad-b0e0-76edd9bbe8df'},

    # 140	d46adbda-7c60-42a0-b1fd-9ec111b35956	Pull Ups on Machine
    # 48	22897ebe-cf17-44cf-97e6-87566285684d	Klimmzüge an Maschine
    {'en': 'd46adbda-7c60-42a0-b1fd-9ec111b35956', 'de': '22897ebe-cf17-44cf-97e6-87566285684d'},

    # 87	d147a6c2-ce64-424b-baf3-4ca841a51512	Dumbbells on Scott Machine
    # 28	d7c553b1-e84d-4dbc-9f6c-05db489b27c8	KH an Scottmaschine
    {'en': 'd147a6c2-ce64-424b-baf3-4ca841a51512', 'de': 'd7c553b1-e84d-4dbc-9f6c-05db489b27c8'},

    # 100	b72ae8d4-ede6-4480-8fc5-7b80e369f7ed	Decline Bench Press Barbell
    # 17	3ef8a516-d0d4-4078-9b4a-d7783da0fcf7	Negativ Bankdrücken
    {'en': 'b72ae8d4-ede6-4480-8fc5-7b80e369f7ed', 'de': '3ef8a516-d0d4-4078-9b4a-d7783da0fcf7'},

    # 101	80d318b3-4b8a-41aa-9c6c-0a2a921fe1e6	Decline Bench Press Dumbbell
    # 720	341c73d5-2e9a-4f13-89c9-c984c86cc088	Negativ Bankdrücken KH
    {'en': '80d318b3-4b8a-41aa-9c6c-0a2a921fe1e6', 'de': '341c73d5-2e9a-4f13-89c9-c984c86cc088'},

    # 318	bd07fc6b-db86-4139-b6de-e328cea0f694	Turkish Get-Up
    # 717	1546af08-017c-4de5-b13f-cb3a1999733d	Turkish Get-Up
    {'en': 'bd07fc6b-db86-4139-b6de-e328cea0f694', 'de': '1546af08-017c-4de5-b13f-cb3a1999733d'},

    # 154	cd4fac32-48fb-4237-a263-a44c5108790a	Leg Curls (laying)
    # 22	8f0170a2-5274-4487-a295-1a9baf2c92a3	Beinbeuger Liegend
    {'en': 'cd4fac32-48fb-4237-a263-a44c5108790a', 'de': '8f0170a2-5274-4487-a295-1a9baf2c92a3'},

    # 118	89c98117-dd53-4334-bfa6-72a96525629a	Leg Curls (standing)
    # 72	9075241c-0493-4f2a-a399-a57e3634093e	Beinbeuger Stehend
    {'en': '89c98117-dd53-4334-bfa6-72a96525629a', 'de': '9075241c-0493-4f2a-a399-a57e3634093e'},

    # 263	9f622058-85a4-4272-ad99-e5696e772137	Roman Chair
    # 714	68f96d3e-9172-468c-9018-06f71a97faff	Beinheben am Roman Chair
    {'en': '9f622058-85a4-4272-ad99-e5696e772137', 'de': '68f96d3e-9172-468c-9018-06f71a97faff'},

    # 421	170cc52f-345f-41b3-bdae-8a5e0c9aa449	Bent-over Lateral Raises
    # 47	e701de98-32c6-4e9d-956d-434cf5bcaaf0	Vorgebeugtes Seitheben
    {'en': '170cc52f-345f-41b3-bdae-8a5e0c9aa449', 'de': 'e701de98-32c6-4e9d-956d-434cf5bcaaf0'},

    # 185	bdb7bdbb-8930-46e5-8b98-eb13e604553f	Squat Jumps
    # 296	032a38cf-b15a-4761-b684-577e41893f54	Tiefe Hocksprünge
    {'en': 'bdb7bdbb-8930-46e5-8b98-eb13e604553f', 'de': '032a38cf-b15a-4761-b684-577e41893f54'},
]


def create_exercise_mapping(apps, schema_editor):
    Exercise = apps.get_model('exercises', 'Exercise')
    ExerciseBase = apps.get_model('exercises', 'ExerciseBase')
    for exercise_group in exercise_mapping:
        langs = list(exercise_group.keys())
        exercise_objects = []
        for lang in langs:
            try:
                exercise_objects.append(Exercise.objects.get(uuid=exercise_group[lang]))
            except Exercise.DoesNotExist:
                print(exercise_group[lang], "does not exist")

        if(len(exercise_objects) > 0):
            exercise_base_main = exercise_objects[0].exercise_base
            for exercise in exercise_objects[1:]:
                ExerciseBase.objects.get(id=exercise.exercise_base.id).delete()
                exercise.exercise_base = exercise_base_main
                exercise.save()


def remove_mappings(apps, schema_editor):
    """
    Backwards migration.
    """
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0010_auto_20201211_0205'),
    ]

    operations = [
        migrations.RunPython(create_exercise_mapping, remove_mappings),
    ]
