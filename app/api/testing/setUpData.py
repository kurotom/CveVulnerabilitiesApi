from api.models import CveModel


def data_testing():
    incorrectObj = CveModel.objects.create(
        name="CVE-0000",
        status="entry",
        description="program with back doors",
        references="http:/url.com/reference",
        phase=" ",
        votes=" ",
        comments=" ",
    )
    incorrectObj.save()

    correctObjformat4 = CveModel.objects.create(
        name="CVE-2004-1111",
        status="entry",
        description="description product random 0101",
        references="http:/url.com/reference",
        phase=" ",
        votes=" ",
        comments=" ",
    )
    correctObjformat4.save()

    correctObjformat6 = CveModel.objects.create(
        name="CVE-2023-111111",
        status="entry",
        description="bug product 1.1",
        references="http:/url.com/reference",
        phase=" ",
        votes=" ",
        comments=" ",
    )
    correctObjformat6.save()
