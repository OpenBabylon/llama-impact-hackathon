import streamlit as st
import time
import pandas as pd

from fireworks.client import Fireworks

FIREWORKS_API_KEY = st.secrets["FIREWORKS_API_KEY"]

# Show title and description.
st.title("Llama-Exam-Tests generator for Ukrainian History")
st.write("Upload a textbook below to generate exam questions")
st.write(
    "Slides [click here](https://pitch.com/v/llama-x-ukrainian-education-f3knrk/11309135-0991-4ca5-a799-626cf95c6bd1)"
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management

if not FIREWORKS_API_KEY:
    st.info("Please add your Fireworks API key to continue.", icon="🗝️")
else:
    # Create an Fireworks client.
    client = Fireworks(api_key=FIREWORKS_API_KEY)

    # Let the user upload a file via `st.file_uploader`.
    uploaded_file = st.file_uploader(
        "Upload your textbook (.txt or .md)", type=("txt", "md")
    )

    # Ask the user for a question via `st.text_area`.
    # question = st.text_area(
    #     "Now ask a question about the document!",
    #     placeholder="Can you give me a short summary?",
    #     disabled=not uploaded_file,
    # )
    document = None
    if st.button("Use example textbook"):
        document = """Український рУх У бУковиНі та закарпатті на початку XX ст. Суспільно-політичне життя тогочасної Буковини значно пожвавилося. Надзвичайною політичною подією в краї стало утворення в 1903 р. в місцевому сеймі «Вільнодумного союзу». Його співзасновниками стали три найвпливовіші по- статі суспільно-політичного життя Буковини — лідер україн- ських народовців Микола Василько, лідер румунських націо- нал-демократів Аурел Ончул і лідер єврейської сіоністської партії Бенно Штраухер. Члени союзу прагнули по-новому розв’язати проблеми краю: вони заявили, що на перше місце висувають вимоги покращення соціально-економічного стано- вища, розширення політичних прав, а також задоволення на- ціональних потреб усіх народів, які населяють Буковину. У 1905 р. через суперечності між його членами союз розпався. 12 листопада 1905 р. буковинські народовці об’єдналися в «Національну раду русинів на Буковині», яку неофіційно на- зивали національно-демократичною партією, підкреслюючи цим ідейну спільність із подібною партією в Галичині. Партія ви- ступала за запровадження загального, рівного й прямого вибор- чого права, у сільському господарстві висувала завдання розви- вати спілчанський рух, обґрунтовуючи національні потреби українців, визнавала таке саме право за іншими націями краю. У червні 1907 р. від «Національної ради русинів на Буко- вині» відокремилося ліве крило й заснувало Радикальну пар- тію. Визволення українського народу ця партія пов’язувала із широкими соціально-економічними перетвореннями та встанов- ленням соціалізму. Майже одночасно в Буковині сформувалася Українська соціал-демократична партія, яка проповідувала ідеї марксизму, вимагала докорінних змін у суспільстві. Однак більшість гасел соціал-демократів були незрозумілі селянам, а робітників у краї було дуже мало.
        У 1907 р. в Буковині відбулися вибори до австрійського парламенту за новим виборчим законом. У всіх українських виборчих округах перемогли кандидати «Національної ради русинів на Буковині». Уперше після 1848 р. буковинські укра- їнці обрали п’ятьох депутатів. У лютому 1910 р. вона об’єд- налася зі створеним С. Смаль-Стоцьким товариством «Руська рада» (її називали також «мужицька партія») у нову партію під назвою «Руська рада». У 1912 р. вона розпалася. Колишні члени «Національної ради» оголосили про створення Націо- нально-демократичної партії, а прибічники С. Смаль- Стоцького — Української народної партії. Однак до початку війни обидві партії остаточно не сформувалися.
        У 1911 р. відбулися останні вибори до Буковинського кра- йового сейму. Із 17 обраних українських депутатів 15 були на- родовцями, по одному від радикалів і соціал-демократів. Моск- вофіли на виборах зазнали поразки.
        Микола Василько
          Аурел Ончул
         Бенно Штраухер
        221
        Розділ VII. Західноукраїнські землі у складі Австро­Угорської імперії на початку XX ст.
          Августин Волошин
        На початку XX ст. в суспільно-політичному житті Закар- паття провідні позиції зберігав москвофільський напрямок. Од- нак у цей час зародилося й народовство. Молоді русинські дія- чі, які заснували його, шукали нові засоби для забезпечення виживання свого народу в умовах мадяризації. Переконавшись у безперспективності москвофільства, вони звинувачували його прибічників у занепаді русинського національного життя в краї. Вирішальним кроком стала відмова закарпатських народовців від використання російської мови та вибір ними як мови освіти й літератури народної мови.
        Друкованим органом народовського руху в краї став тиж- невик «Наука», що виходив із 1897 р. Його головним редак- тором із 1903 р. був Августин Волошин (1874—1945), який згодом відіграв визначну роль в історії Закарпаття.
        Розвиток народовства в краї відбувався під впливом і в тіс- ній взаємодії з українським рухом Галичини. Зокрема, праці закарпатських учених і громадських діячів друкувалися у ви- даннях Наукового товариства ім. Т. Шевченка у Львові, а гро- мадські діячі Галичини (І. Франко, С. Томашівський, В. Гна- тюк та інші) докладали чимало зусиль для ознайомлення світової громадськості з безправним становищем закарпатських русинів.
        Роль народовців на початку століття в суспільно-політич- ному житті Закарпаття була досить непомітною. Їх діяльність обмежувалася питаннями мови, літератури, історії й освіти. Вони не прагнули надання краю автономії або самоврядування, не виступали за його приєднання до решти українських земель. Головним завданням народовці вважали зберегти ті прояви на- ціонального життя, які в майбутньому сприятимуть відроджен- ню Закарпаття.
        """

    if uploaded_file:
        # Process the uploaded file and question.
        document = uploaded_file.read().decode()

    if document:
        messages_en = [
            {
                "role": "user",
                "content": f"""You are a highly skilled history professor with expertise in Ukrainian history. Your task is to generate multiple choice questions based on the provided text. Follow these specific requirements:

                Please analyze the following text from a Ukrainian history textbook:
                {document}

                Output Requirements
                Generate 10 multiple choice questions that:

                Directly reference information from the provided text
                Include exactly 4 options (A, B, C, D) per question
                Have exactly one correct answer
                Maintain consistent difficulty appropriate for [GRADE LEVEL] students

                For each question, provide:

                - Question number
                - Question text
                - Four answer choices (labeled A-D)
                - The correct answer (marked with *)
                - Brief explanation of why the correct answer is right and why the distractors are wrong

                Question Distribution
                Generate questions in this ratio:

                3 questions testing factual recall
                3 questions testing comprehension/understanding
                2 questions testing analysis/interpretation
                2 questions testing cause-and-effect relationships

                Answer Choice Guidelines

                All distractors must be historically plausible
                Maintain similar length and grammatical structure
                Avoid absolutes (always, never, all, none)
                Each distractor should represent a common misconception or partial understanding
                Ensure historical accuracy in all options, even incorrect ones

                Format Each Question As:
                Q[number]: [Question text]

                A) [Option A]
                B) [Option B]
                C) [Option C]
                D) [Option D]

                Correct Answer: [Letter]

                Explanation:
                - Why correct answer is right: [brief explanation]
                - Why other options are wrong: [brief explanation for each]

                Question Type: [Factual/Comprehension/Analysis/Cause-Effect]
                Additional Parameters:

                - Use clear, grade-appropriate language
                - Include relevant dates and context
                - Avoid negative phrasing
                - Focus on significant historical developments
                - Balance questions between political, social, cultural, and economic aspects
                - Ensure questions progress from simpler to more complex concepts
                """,
            }
        ]
        messages_ua = [
            {
                "role": "user",
                "content": f"""Ви – висококваліфікований професор історії, що спеціалізується на українській історії. Ваше завдання – створити запитання з багатьма відповідями на основі наданого тексту.
                Дотримуйтесь наступних вимог:
                Проаналізуйте наступний текст з підручника з історії України:

                {document}

                Вимоги до результату
                Створіть 10 запитань з множинним вибором, які:

                Безпосередньо посилаються на інформацію з наданого тексту
                Містять рівно 4 варіанти відповіді (А, Б, В, Г) для кожного запитання
                Мають лише одну правильну відповідь

                - Для кожного запитання вкажіть:
                - Номер запитання
                - Текст запитання
                - Чотири варіанти відповіді (позначені А-Г)
                - Правильну відповідь (позначену *)
                - Коротке пояснення, чому відповідь правильна та чому інші варіанти неправильні

                Розподіл запитань

                Створіть запитання у такому співвідношенні:

                3 запитання для перевірки фактологічної інформації
                3 запитання для перевірки розуміння
                2 запитання для перевірки аналізу та інтерпретації
                2 запитання для перевірки причинно-наслідкових зв’язків

                Вимоги до варіантів відповідей

                Усі дистрактори мають бути історично правдоподібними
                Відповіді мають бути однакової довжини та граматичної структури
                Уникайте абсолютів (завжди, ніколи, усі, жоден)
                Кожен дистрактор повинен відображати поширену помилку або часткове розуміння
                Забезпечте історичну точність у всіх варіантах, навіть неправильних

                Формат кожного запитання:
                П[номер]: [Текст запитання]

                А) [Варіант А]
                Б) [Варіант Б]
                В) [Варіант В]
                Г) [Варіант Г]

                Правильна відповідь: [Літера]

                Пояснення:
                Чому правильна відповідь правильна: [коротке пояснення]
                Чому інші варіанти неправильні: [коротке пояснення для кожного]

                Тип запитання: [Фактологічне/Розуміння/Аналіз/Причинно-наслідкове]
                Додаткові параметри:

                - Використовуйте чітку, відповідну для рівня учнів мову
                - Включайте важливі дати та контекст
                - Уникайте заперечних формулювань
                - Зосереджуйтеся на значних історичних подіях
                - Балансуйте запитання між політичними, соціальними, культурними та економічними аспектами
                - Забезпечте поступовий перехід від простих до складніших понять
                """,
            }
        ]
        st.write("=======ENGLISH===========")
        with st.spinner("Performing task in EN..."):
            start_time = time.time()
            response = client.chat.completions.create(
                model="accounts/fireworks/models/llama-v3p1-8b-instruct",
                messages=messages_en,
            )
            execution_time_en = time.time() - start_time
            response_tokens_en = response.usage.completion_tokens
            response_chars_en = len(response.choices[0].message.content)

            output_text = response.choices[0].message.content
            # print(output_text)
            st.write(output_text)

        st.write("=======Ukrainian=========")
        with st.spinner("Performing task in UA..."):
            start_time = time.time()
            response = client.chat.completions.create(
                model="accounts/fireworks/models/llama-v3p1-8b-instruct",
                messages=messages_ua,
            )
            execution_time_ua = time.time() - start_time
            response_tokens_ua = response.usage.completion_tokens
            response_chars_ua = len(response.choices[0].message.content)

            output_text = response.choices[0].message.content
            # print(output_text)
            st.write(output_text)

        # st.write("=======Inference Stats=========")
        # df = pd.DataFrame(
        #     [
        #         (
        #             "en",
        #             response_chars_en,
        #             # response_chars_en / execution_time_en,
        #             response_tokens_en,
        #             # response_tokens_en / execution_time_en,
        #             response_chars_en / response_tokens_en,
        #         ),
        #         (
        #             "ua",
        #             response_chars_ua,
        #             # response_chars_ua / execution_time_ua,
        #             response_tokens_ua,
        #             # response_tokens_ua / execution_time_ua,
        #             response_chars_ua / response_tokens_ua,
        #         ),
        #     ],
        #     columns=[
        #         "language",
        #         "chars generated",
        #         # "chars/s",
        #         "tokens used",
        #         # "tok/s",
        #         "char/tok",
        #     ],
        # )

        # st.table(df)
