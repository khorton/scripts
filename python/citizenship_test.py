#! /usr/bin/env python

import random
import sys

test = [{"Q": '1. What is the supreme law of the land?', "A": ' ▪ the Constitution'}, 
        {"Q": '2. What does the Constitution do?', "A": ' ▪ sets up the government \n ▪ defines the government \n ▪ protects basic rights of Americans'},
        {"Q": '3. The idea of self-government is in the first three words of the Constitution.  What are these words?', "A": ' ▪ We the People'},
        {"Q": '4. What is an amendment?', "A": ' ▪ a change (to the Constitution) \n ▪ an addition (to the Constitution)'},
        {"Q": '5. What do we call the first ten amendments to the Constitution?', "A": ' ▪ the Bill of Rights'},
        {"Q": '6. What is one right or freedom from the First Amendment?', "A": ' ▪ speech \n ▪ religion \n ▪ assembly \n ▪ press \n ▪ petition the government'},
        {"Q": '7. How many amendments does the Constitution have?', "A": ' ▪ twenty-seven (27)'},
        {"Q": '8. What did the Declaration of Independence do?', "A": ' ▪ announced our independence (from Great Britain) \n ▪ declared our independence (from Great Britain) \n ▪ said that the United States is free (from Great Britain)'},
        {"Q": '9. What are two rights in the Declaration of Independence?', "A": ' ▪ life \n ▪ liberty \n ▪ pursuit of happiness'},
        {"Q": '10. What is freedom of religion?', "A": ' ▪ You can practice any religion, or not practice a religion.'},
        {"Q": '11. What is the economic system in the United States?', "A": ' ▪ capitalist economy \n ▪ market economy'},
        {"Q": '12. What is the “rule of law”?', "A": ' ▪ Everyone must follow the law. \n ▪ Leaders must obey the law. \n ▪ Government must obey the law. \n ▪ No one is above the law.'},
        {"Q": '13. Name one branch or part of the government.', "A": ' ▪ Congress \n ▪ legislative \n ▪ President \n ▪ executive \n ▪ the courts \n ▪ judicial'},
        {"Q": '14. What stops one branch of government from becoming too powerful?', "A": ' ▪ checks and balances \n ▪ separation of powers'},
        {"Q": '15. Who is in charge of the executive branch?', "A": ' ▪ the President'},
        {"Q": '16. Who makes federal laws?', "A": ' ▪ Congress \n ▪ Senate and House (of Representatives) \n ▪ (U.S. or national) legislature'},
        {"Q": '17. What are the two parts of the U.S. Congress?', "A": ' ▪ the Senate and House (of Representatives)'},
        {"Q": '18. How many U.S. Senators are there?', "A": ' ▪ one hundred (100)'},
        {"Q": '19. We elect a U.S. Senator for how many years?', "A": ' ▪ six (6)'},
        {"Q": '20. Who is one of your state’s U.S. Senators now?', "A": ' ▪ Ron Johnson \n ▪ Tammy Baldwin'},
        {"Q": '21. The House of Representatives has how many voting members?', "A": ' ▪ four hundred thirty-five (435)'},
        {"Q": '22. We elect a U.S. Representative for how many years?', "A": ' ▪ two (2)'},
        {"Q": '23. Name your U.S. Representative.', "A": ' ▪ Mike Gallagher'},
        {"Q": '24. Who does a U.S. Senator represent?', "A": ' ▪ all people of the state'},
        {"Q": '25. Why do some states have more Representatives than other states?', "A": ' ▪ (because of) the state’s population\n ▪ (because) they have more people \n ▪ (because) some states have more people'},
        {"Q": '26. We elect a President for how many years?', "A": ' ▪ four (4)'},
        {"Q": '27. In what month do we vote for President?', "A": ' ▪ November'},
        {"Q": '28. What is the name of the President of the United States now?', "A": ' ▪ Joe Biden'},
        {"Q": '29. What is the name of the Vice President of the United States now?', "A": ' ▪ Kamala Harris'},
        {"Q": '30. If the President can no longer serve, who becomes President?', "A": ' ▪ the Vice President'},
        {"Q": '31. If both the President and the Vice President can no longer serve, who becomes President?', "A": ' ▪ the Speaker of the House'},
        {"Q": '32. Who is the Commander in Chief of the military?', "A": ' ▪ the President'},
        {"Q": '33. Who signs bills to become laws?', "A": ' ▪ the President'},
        {"Q": '34. Who vetoes bills?', "A": ' ▪ the President'},
        {"Q": '35. What does the President’s Cabinet do?', "A": ' ▪ advises the President'},
        {"Q": '36. What are two Cabinet-level positions?', "A": ' ▪ Secretary of Agriculture \n ▪ Secretary of Commerce \n ▪ Secretary of Defense \n ▪ Secretary of Education \n ▪ Secretary of Energy \n ▪ Secretary of Health and Human Services \n ▪ Secretary of Homeland Security \n ▪ Secretary of Housing and Urban Development \n ▪ Secretary of the Interior \n ▪ Secretary of Labor \n ▪ Secretary of State \n ▪ Secretary of Transportation \n ▪ Secretary of the Treasury \n ▪ Secretary of Veterans Affairs \n ▪ Attorney General \n ▪ Vice President '},
        {"Q": '37. What does the judicial branch do?', "A": ' ▪ reviews laws \n ▪ explains laws \n ▪ resolves disputes (disagreements) \n ▪ decides if a law goes against the Constitution'},
        {"Q": '38. What is the highest court in the United States?', "A": ' ▪ the Supreme Court'},
        {"Q": '39. How many justices are on the Supreme Court?', "A": ' ▪ nine'},
        {"Q": '40. Who is the Chief Justice of the United States now?', "A": ' ▪ John Roberts'},
        {"Q": '41. Under our Constitution, some powers belong to the federal government. What is one power of the federal government?', "A": ' ▪ to print money \n ▪ to declare war \n ▪ to create an army \n ▪ to make treaties'},
        {"Q": '42. Under our Constitution, some powers belong to the states. What is one power of the states?', "A": ' ▪ provide schooling and education \n ▪ provide protection (police) \n ▪ provide safety (fire departments) \n ▪ give a driver’s license \n ▪ approve zoning and land use'},
        {"Q": '43. Who is the Governor of your state now?', "A": ' ▪ Tony Evers'},
        {"Q": '44. What is the capital of your state?', "A": ' ▪ Madison, WI'},
        {"Q": '45. What are the two major political parties in the United States?', "A": ' ▪ Democratic and Republican'},
        {"Q": '46. What is the political party of the President now?', "A": ' ▪ Democratic Party'},
        {"Q": '47. What is the name of the Speaker of the House of Representatives now?', "A": ' ▪ Mike Johnson'},
        {"Q": '48. There are four amendments to the Constitution about who can vote. Describe one of them.', "A": ' ▪ Citizens eighteen (18) and older (can vote).\n ▪ You don’t have to pay (a poll tax) to vote. \n ▪ Any citizen can vote. (Women and men can vote.) \n ▪ A male citizen of any race (can vote).'},
        {"Q": '49. What is one responsibility that is only for United States citizens?', "A": ' ▪ serve on a jury\n ▪ vote in a federal election'},
        {"Q": '50. Name one right only for United States citizens.', "A": ' ▪ vote in a federal election\n ▪ run for federal office'},
        {"Q": '51. What are two rights of everyone living in the United States?', "A": ' ▪ freedom of expression \n ▪ freedom of speech \n ▪ freedom of assembly \n ▪ freedom to petition the government\n ▪ freedom of religion \n ▪ the right to bear arms'},
        {"Q": '52. What do we show loyalty to when we say the Pledge of Allegiance?', "A": ' ▪ the United States \n ▪ the flag'},
        {"Q": '53. What is one promise you make when you become a United States citizen?', "A": ' ▪ give up loyalty to other countries \n ▪ defend the Constitution and laws of the United States \n ▪ obey the laws of the United States \n ▪ serve in the U.S. military (if needed) \n ▪ serve (do important work for) the nation (if needed) \n ▪ be loyal to the United States'},
        {"Q": '54. How old do citizens have to be to vote for President?', "A": ' ▪ eighteen (18) and older'},
        {"Q": '55. What are two ways that Americans can participate in their democracy?', "A": ' ▪ vote \n ▪ join a political party \n ▪ help with a campaign \n ▪ join a civic group \n ▪ join a community group \n ▪ give an elected official your opinion on an issue \n ▪ call Senators and Representatives \n ▪ publicly support or oppose an issue or policy \n ▪ run for office \n ▪ write to a newspaper'},
        {"Q": '56. When is the last day you can send in federal income tax forms?', "A": ' ▪ April 15'},
        {"Q": '57. When must all men register for the Selective Service?', "A": ' ▪ at age eighteen (18) \n ▪ between eighteen (18) and twenty-six (26)'},
        {"Q": '58. What is one reason colonists came to America?', "A": ' ▪ freedom \n ▪ political liberty \n ▪ religious freedom \n ▪ economic opportunity \n ▪ practice their religion \n ▪ escape persecution'},
        {"Q": '59. Who lived in America before the Europeans arrived?', "A": ' ▪ American Indians \n ▪ Native Americans'},
        {"Q": '60. What group of people was taken to America and sold as slaves?', "A": ' ▪ Africans \n ▪ people from Africa'},
        {"Q": '61. Why did the colonists fight the British?', "A": ' ▪ because of high taxes (taxation without representation) \n ▪ because the British army stayed in their houses (boarding, quartering) \n ▪ because they didn’t have self-government'},
        {"Q": '62. Who wrote the Declaration of Independence?', "A": ' ▪ (Thomas) Jefferson'},
        {"Q": '63. When was the Declaration of Independence adopted?', "A": ' ▪ July 4, 1776'},
        {"Q": '64. There were 13 original states. Name three.', "A": ' ▪ New Hampshire \n ▪ Massachusetts \n ▪ Rhode Island \n ▪ Connecticut \n ▪ New York \n ▪ New Jersey \n ▪ Pennsylvania \n ▪ Delaware \n ▪ Maryland \n ▪ Virginia \n ▪ North Carolina \n ▪ South Carolina \n ▪ Georgia'},
        {"Q": '65. What happened at the Constitutional Convention?', "A": ' ▪ The Constitution was written. \n ▪ The Founding Fathers wrote the Constitution.'},
        {"Q": '66. When was the Constitution written?', "A": ' ▪ 1787'},
        {"Q": '67. The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers.', "A": ' ▪ (James) Madison \n ▪ (Alexander) Hamilton \n ▪ (John) Jay \n ▪ Publius'},
        {"Q": '68. What is one thing Benjamin Franklin is famous for?', "A": ' ▪ U.S. diplomat \n ▪ oldest member of the Constitutional Convention\n ▪ first Postmaster General of the United States \n ▪ writer of “Poor Richard’s Almanac” \n ▪ started the first free libraries'},
        {"Q": '69. Who is the “Father of Our Country”?', "A": ' ▪ (George) Washington'},
        {"Q": '70. Who was the first President?', "A": ' ▪ (George) Washington'},
        {"Q": '71. What territory did the United States buy from France in 1803?', "A": ' ▪ the Louisiana Territory \n ▪ Louisiana'},
        {"Q": '72. Name one war fought by the United States in the 1800s.', "A": ' ▪ War of 1812 \n ▪ Mexican-American War \n ▪ Civil War \n ▪ Spanish-American War'},
        {"Q": '73. Name the U.S. war between the North and the South.', "A": ' ▪ the Civil War \n ▪ the War between the States'},
        {"Q": '74. Name one problem that led to the Civil War.', "A": ' ▪ slavery \n ▪ economic reasons \n ▪ states’ rights'},
        {"Q": '75. What was one important thing that Abraham Lincoln did?', "A": ' ▪ freed the slaves (Emancipation Proclamation) \n ▪ saved (or preserved) the Union  ▪ led the United States during the Civil War'},
        {"Q": '76. What did the Emancipation Proclamation do?', "A": ' ▪ freed the slaves \n ▪ freed slaves in the Confederacy \n ▪ freed slaves in the Confederate states \n ▪ freed slaves in most Southern states'},
        {"Q": '77. What did Susan B. Anthony do?', "A": ' ▪ fought for women’s rights \n ▪ fought for civil rights'},
        {"Q": '78. Name one war fought by the United States in the 1900s.', "A": ' ▪ World War I \n ▪ World War II \n ▪ Korean War \n ▪ Vietnam War \n ▪ (Persian) Gulf War'},
        {"Q": '79. Who was President during World War I?', "A": ' ▪ (Woodrow) Wilson'},
        {"Q": '80. Who was President during the Great Depression and World War II?', "A": ' ▪ (Franklin) Roosevelt'},
        {"Q": '81. Who did the United States fight in World War II?', "A": ' ▪ Japan, Germany, and Italy'},
        {"Q": '82. Before he was President, Eisenhower was a general. What war was he in?', "A": ' ▪ World War II'},
        {"Q": '83. During the Cold War, what was the main concern of the United States?', "A": ' ▪ Communism'},
        {"Q": '84. What movement tried to end racial discrimination?', "A": ' ▪ civil rights (movement)'},
        {"Q": '85. What did Martin Luther King, Jr. do?', "A": ' ▪ fought for civil rights \n ▪ worked for equality for all Americans'},
        {"Q": '86. What major event happened on September 11, 2001, in the United States?', "A": ' ▪ Terrorists attacked the United States.'},
        {"Q": '87. Name one American Indian tribe in the United States.', "A": ' ▪ Cherokee \n ▪ Navajo \n ▪ Sioux \n ▪ Chippewa \n ▪ Choctaw \n ▪ Pueblo \n ▪ Apache \n ▪ Iroquois \n ▪ Creek \n ▪ Blackfeet \n ▪ Seminole \n ▪ Cheyenne \n ▪ Arawak \n ▪ Shawnee \n ▪ Mohegan \n ▪ Huron \n ▪ Oneida \n ▪ Lakota \n ▪ Crow \n ▪ Teton \n ▪ Hopi \n ▪ Inuit \n'},
        {"Q": '88. Name one of the two longest rivers in the United States.', "A": ' ▪ Missouri (River) \n ▪ Mississippi (River)'},
        {"Q": '89. What ocean is on the West Coast of the United States?', "A": ' ▪ Pacific (Ocean)'},
        {"Q": '90. What ocean is on the East Coast of the United States?', "A": ' ▪ Atlantic (Ocean)'},
        {"Q": '91. Name one U.S. territory.', "A": ' ▪ Puerto Rico \n ▪ U.S. Virgin Islands \n ▪ American Samoa \n ▪ Northern Mariana Islands \n ▪ Guam'},
        {"Q": '92. Name one state that borders Canada.', "A": ' ▪ Maine \n ▪ New Hampshire \n ▪ Vermont \n ▪ New York \n ▪ Pennsylvania \n ▪ Ohio \n ▪ Michigan \n ▪ Minnesota \n ▪ North Dakota \n ▪ Montana \n ▪ Idaho \n ▪ Washington \n ▪ Alaska \n'},
        {"Q": '93. Name one state that borders Mexico.', "A": ' ▪ California \n ▪ Arizona \n ▪ New Mexico \n ▪ Texas'},
        {"Q": '94. What is the capital of the United States?', "A": ' ▪ Washington, D.C.'},
        {"Q": '95. Where is the Statue of Liberty?', "A": ' ▪ New York (Harbor) \n ▪ Liberty Island'},
        {"Q": '96. Why does the flag have 13 stripes?', "A": ' ▪ because there were 13 original colonies \n ▪ because the stripes represent the original colonies'},
        {"Q": '97. Why does the flag have 50 stars?', "A": ' ▪ because there is one star for each state \n ▪ because each star represents a state \n ▪ because there are 50 states'},
        {"Q": '98. What is the name of the national anthem?', "A": ' ▪ The Star-Spangled Banner'},
        {"Q": '99. When do we celebrate Independence Day?', "A": ' ▪ July 4'},
        {"Q": '100. Name two national U.S. holidays.', "A": ' ▪ New Year’s Day \n ▪ Martin Luther King, Jr. Day \n ▪ Presidents’ Day \n ▪ Memorial Day \n ▪ Juneteenth \n ▪ Independence Day \n ▪ Labor Day \n ▪ Columbus Day \n ▪ Veterans Day \n ▪ Thanksgiving \n ▪ Christmas'},
]

def do_test(n=100, Type = 'Random', Start = 1):
    Start -= 1
    if Type == 'Random':
        random_test = random.sample(test, n)
    else:
        random_test = test
#     while(true):
#         a = keyboard.read_key()
#         if a == 'q':
#             sys.exit()
#         if a == 
    ques = Start
    step = 0
    print('Press Return to run test.  Q to quit\n')
    while(ques < n + Start):
        key = input('')
        if key == 'q' or key == 'Q':
            sys.exit()
        elif key =="":
            if step == 0:
                print(random_test[ques]["Q"])
                step += 1
            else:
                print(random_test[ques]["A"])
                step = 0
                ques += 1
            
        else:
            pass
        

