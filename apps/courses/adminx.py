# -*- encoding: utf-8 -*-

import xadmin
from xadmin.layout import Fieldset, Main, Row, Side
from .models import Course, Lesson, Video, CourseResource


# 在课程页面可以不断添加章节的内容，嵌套一层，不能多层嵌套
class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    # 列表展示可以显示函数
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'student', 'fav_nums', 'click_nums', 'is_disable', 'create_time', 'update_time']
    # 搜索的字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times',
                     'student', 'fav_nums', 'click_nums', 'is_disable']
    # 过滤的字段
    list_filter = list_display
    # 查看详情的字段
    show_detail_fields = ['name']
    # 排序字段设置
    ordering = ['-click_nums', 'create_time']
    # 某些字段我们只能查看，不能修改
    readonly_fields = ['learn_times', 'create_time', 'update_time']
    # 设置某些字段在详情里不显示，不能与只读字段相同，不然不起作用
    exclude = ['click_nums']
    # 在课程页面可以不断添加章节的内容
    inlines = [LessonInline, CourseResourceInline]
    # 可以直接在列表页面对某些字段进行修改
    list_editable = ['desc', 'detail', 'degree', 'is_disable']
    # 定时刷新
    # refresh_times = [3, 5]
    # 是否显示书签
    show_bookmarks = False
    # 书签列表配置
    list_bookmarks = [{}]
    # 指定菜单的 icon
    model_icon = 'fa fa-circle-o'


class NewCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'student', 'fav_nums', 'click_nums', 'is_disable', 'create_time', 'update_time']
    # 搜索的字段
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times',
                     'student', 'fav_nums', 'click_nums', 'is_disable']
    # 过滤的字段
    list_filter = list_display

    def queryset(self):
        qs = super().queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(teacher=self.request.user.teacher)
        return qs

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                    Main(
                        Fieldset("讲师信息",
                                 'teacher','course_org',
                                 css_class='unsort no_title'
                                 ),
                        Fieldset("基本信息",
                                 'name', 'desc',
                                 Row('learn_times', 'degree'),
                                 Row('category', 'tag'),
                                 'youneed_know', 'teacher_tell', 'detail',
                                 ),
                    ),
                    Side(
                        Fieldset("访问信息",
                                 'fav_nums', 'click_nums', 'student','add_time'
                                 ),
                    ),
                    Side(
                        Fieldset("选择信息",
                                 'is_banner', 'is_classics'
                                 ),
                    )
            )
        return super(NewCourseAdmin, self).get_form_layout()


class LessonAdmin(object):
    list_display = ['course', 'name', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'create_time']
    show_detail_fields = ['name']
    list_editable = ['name']
    show_bookmarks = False


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'url', 'create_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'create_time']
    show_detail_fields = ['name']
    list_editable = ['name', 'url']
    show_bookmarks = False
    model_icon = 'fa fa-play-circle'


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'create_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'file', 'create_time']
    show_detail_fields = ['name']
    list_editable = ['name']
    show_bookmarks = False


xadmin.site.register(Course, NewCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
