# -*- coding: utf-8 -*

from mamba import describe, context

from expects import expect
from expects.testing import failure


with describe('true'):
    def it_should_pass_if_actual_is_true():
        expect(True).to.be.true

    def it_should_fail_if_actual_is_false():
        with failure(False, 'to be True'):
            expect(False).to.be.true

    with context('#negated'):
        def it_should_pass_if_actual_is_not_true():
            expect(False).not_to.be.true

        def it_should_fail_if_actual_is_true():
            with failure(True, 'not to be True'):
                expect(True).not_to.be.true
