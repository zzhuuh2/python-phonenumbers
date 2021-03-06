"""Auto-generated file, do not edit by hand. AU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AU = PhoneMetadata(id='AU', country_code=61, international_prefix='(?:14(?:1[14]|34|4[17]|[56]6|7[47]|88))?001[14-689]',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-578]\\d{5,9}', possible_number_pattern='\\d{6,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='[237]\\d{8}|8(?:[68]\\d{3}|7[0-69]\\d{2}|9(?:[02-9]\\d{2}|1(?:[0-57-9]\\d|6[0135-9])))\\d{4}', possible_number_pattern='\\d{8,9}', example_number='212345678'),
    mobile=PhoneNumberDesc(national_number_pattern='14(?:5\\d|71)\\d{5}|4(?:[0-2]\\d|3[0-57-9]|4[47-9]|5[0-35-9]|6[6-9]|[79][07-9]|8[17-9])\\d{6}', possible_number_pattern='\\d{9}', example_number='412345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='180(?:0\\d{3}|2)\\d{3}', possible_number_pattern='\\d{7,10}', example_number='1800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='190[0126]\\d{6}', possible_number_pattern='\\d{10}', example_number='1900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='13(?:00\\d{2})?\\d{4}', possible_number_pattern='\\d{6,10}', example_number='1300123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='500\\d{6}', possible_number_pattern='\\d{9}', example_number='500123456'),
    voip=PhoneNumberDesc(national_number_pattern='550\\d{6}', possible_number_pattern='\\d{9}', example_number='550123456'),
    pager=PhoneNumberDesc(national_number_pattern='16\\d{3,7}', possible_number_pattern='\\d{5,9}', example_number='1612345'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='1(?:3(?:\\d{4}|00\\d{6})|80(?:0\\d{6}|2\\d{3}))', possible_number_pattern='\\d{6,10}', example_number='1300123456'),
    preferred_international_prefix='0011',
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([2378])(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2378]'], national_prefix_formatting_rule=u'(0\\1)'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[45]|14'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(16)(\\d{3})(\\d{2,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['16'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(1[389]\\d{2})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1(?:[38]0|90)', '1(?:[38]00|90)'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(180)(2\\d{3})', format=u'\\1 \\2', leading_digits_pattern=['180', '1802'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(19\\d)(\\d{3})', format=u'\\1 \\2', leading_digits_pattern=['19[13]'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(19\\d{2})(\\d{4})', format=u'\\1 \\2', leading_digits_pattern=['19[67]'], national_prefix_formatting_rule=u'\\1'),
        NumberFormat(pattern='(13)(\\d{2})(\\d{2})', format=u'\\1 \\2 \\3', leading_digits_pattern=['13[1-9]'], national_prefix_formatting_rule=u'\\1')],
    main_country_for_code=True,
    mobile_number_portable_region=True)
