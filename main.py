from manim import *

class Scene1(Scene):
    def construct(self):
        title = Text("Scene 1: Yitro arrives with Moshe's family", font_size=36)
        self.play(Write(title))
        self.wait(1)
        title.generate_target()
        title.target = title.to_edge(UP)
        self.play(MoveToTarget(title))

        description = Text("Yitro arrives with Moshe's family in the desert.", font_size=28)
        self.play(Write(description))
        self.wait(1)
        bible_text = Text("יבא יתרו חתן משה ובניו ואשתו אל־משה אל־המדבר...", font_size=24)
        self.play(FadeOut(description), FadeIn(bible_text))
        self.wait(3)

class Scene2(Scene):
    def construct(self):
        title = Text("Scene 2: Moshe judges the people", font_size=36)
        self.play(Write(title))
        self.wait(1)
        title.generate_target()
        title.target = title.to_edge(UP)
        self.play(MoveToTarget(title))

        description = Text("Moshe sits to judge the people, with a long line from morning to evening.", font_size=28)
        self.play(Write(description))
        self.wait(1)
        bible_text = Text("ויהי ממחרת וישב משה לשפט את־העם ויעמד העם על־משה מן־הבקר עד־הערב", font_size=24)
        self.play(FadeOut(description), FadeIn(bible_text))
        self.wait(3)

class Scene3(Scene):
    def construct(self):
        title = Text("Scene 3: Yitro observes", font_size=36)
        self.play(Write(title))
        self.wait(1)
        title.generate_target()
        title.target = title.to_edge(UP)
        self.play(MoveToTarget(title))

        description = Text("Yitro observes the situation, concerned.", font_size=28)
        self.play(Write(description))
        self.wait(1)
        bible_text = Text("וירא חתן משה את כל־אשר־הוא עשה לעם ויאמר מה־הדבר הזה אשר אתה עשה לעם מדוע אתה יושב לבדך וכל־העם נצב עליך מן־בקר עד־ערב", font_size=24)
        self.play(FadeOut(description), FadeIn(bible_text))
        self.wait(3)

class Scene4(Scene):
    def construct(self):
        title = Text("Scene 4: Moshe explains", font_size=36)
        self.play(Write(title))
        self.wait(1)
        title.generate_target()
        title.target = title.to_edge(UP)
        self.play(MoveToTarget(title))

        description = Text("Moshe explains the situation to Yitro.", font_size=28)
        self.play(Write(description))
        self.wait(1)
        bible_text_1 = Text("ויאמר משה לחתנו כי־יבא אלי העם לדרש אלהים", font_size=24)
        bible_text_2 = Text("כי־יהיה להם דבר בא אלי ושפטתי בין איש ובין רעהו והודעתי את־חקי האלהים ואת־תורתיו", font_size=24).next_to(bible_text_1, DOWN)
        self.play(FadeOut(description), FadeIn(bible_text_1), FadeIn(bible_text_2))
        self.wait(3)

class Scene5(Scene):
    def construct(self):
        title = Text("Scene 5: Yitro advises", font_size=36)
        self.play(Write(title))
        self.wait(1)
        title.generate_target()
        title.target = title.to_edge(UP)
        self.play(MoveToTarget(title))

        description = Text("Yitro scolds Moshe and advises him.", font_size=28)
        self.play(Write(description))
        self.wait(1)
        bible_text_1 = Text("ויאמר חתן משה אליו לא־טוב הדבר אשר אתה עשה", font_size=24)
        bible_text_2 = Text("נבל תבל גם־אתה גם־העם הזה אשר עמך כי־כבד ממך הדבר לא־תוכל עשהו לבדך", font_size=24).next_to(bible_text_1, DOWN)
        self.play(FadeOut(description), FadeIn(bible_text_1), FadeIn(bible_text_2))
        self.wait(3)

class Scene6(Scene):
    def construct(self):
        title = Text("Scene 6: Yitro's advice", font_size=36)
        self.play(Write(title))
        self.wait(1)
        title.generate_target()
        title.target = title.to_edge(UP)
        self.play(MoveToTarget(title))

        description = Text("Yitro advises Moshe to appoint leaders.", font_size=28)
        self.play(Write(description))
        self.wait(1)
        bible_text_1 = Text("ואתה תחזה מכל־העם אנשי־חיל יראי אלהים אנשי אמת שנאי בצע ושמת עלהם שרי אלפים שרי מאות שרי חמשים ושרי עשרת", font_size=24)
        bible_text_2 = Text("ושפטו את־העם בכל־עת והיה כל־הדבר הגדל יביאו אליך וכל־הדבר הקטן ישפטו־הם והקל מעליך ונשאו אתך", font_size=24).next_to(bible_text_1, DOWN)
        self.play(FadeOut(description), FadeIn(bible_text_1), FadeIn(bible_text_2))
        self.wait(3)

class Scene7(Scene):
    def construct(self):
        title = Text("Scene 7: Moshe appoints leaders", font_size=36)
        self.play(Write(title))
        self.wait(1)
        title.generate_target()
        title.target = title.to_edge(UP)
        self.play(MoveToTarget(title))

        description = Text("Moshe appoints leaders and the community gets their questions answered efficiently.", font_size=28)
        self.play(Write(description))
        self.wait(1)
        bible_text = Text("וישמע משה לקול חתנו ויעש כל אשר אמר", font_size=24)
        self.play(FadeOut(description), FadeIn(bible_text))
        self.wait(3)

class Scene8(Scene):
    def construct(self):
        title = Text("Scene 8: Moral of the story", font_size=36)
        self.play(Write(title))
        self.wait(1)
        title.generate_target()
        title.target = title.to_edge(UP)
        self.play(MoveToTarget(title))

        description = Text("Just like Moshe, in the Actor Model, don’t let one actor handle everything. Distribute the tasks among many small actors to keep things running smoothly.", font_size=28)
        self.play(Write(description))
        self.wait(3)

        self.play(FadeOut(description))
        moral_text = Text("The moral of the story? Distribute the tasks among many small actors.", font_size=24)
        self.play(Write(moral_text))
        self.wait(3)
